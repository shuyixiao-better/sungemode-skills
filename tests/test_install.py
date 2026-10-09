import contextlib
import importlib.util
import io
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)
NAMES = sorted(path.name for path in (ROOT / "skills").iterdir() if path.is_dir())


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.dest = self.base / "skills"

    def install(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install([self.dest], NAMES, **kwargs)

    def cli(self, *args):
        return subprocess.run([sys.executable, str(ROOT / "scripts/install.py"), *args], capture_output=True, text=True)

    def test_both_languages_materialize_complete_local_packages(self):
        for lang in ("zh", "en"):
            target = self.base / lang
            with contextlib.redirect_stdout(io.StringIO()):
                installer.install([target], NAMES, lang)
            for name in NAMES:
                source = ROOT / "skills" / name
                package = target / name
                expected = source / ("SKILL.en.md" if lang == "en" else "SKILL.md")
                self.assertEqual((package / "SKILL.md").read_bytes(), expected.read_bytes())
                self.assertEqual((package / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())
                ui = "openai.en.yaml" if lang == "en" else "openai.yaml"
                self.assertEqual((package / "agents/openai.yaml").read_bytes(), (source / "agents" / ui).read_bytes())
                for doc in package.rglob("*.md"):
                    for href in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", doc.read_text(encoding='utf-8')):
                        if "://" not in href:
                            resolved = (doc.parent / href.split("#", 1)[0]).resolve()
                            self.assertTrue(resolved.is_relative_to(package.resolve()))
                            self.assertTrue(resolved.exists(), (doc, href))
                self.assertFalse((package / "SKILL.en.md").exists())

    def test_dry_run_writes_nothing(self):
        self.install(dry_run=True)
        self.assertFalse(self.dest.exists())

    def test_repeated_install_preserves_files_and_timestamps(self):
        self.install()
        entry = self.dest / "sungemode/SKILL.md"
        original = entry.read_bytes(), entry.stat().st_mtime_ns
        self.install()
        self.assertEqual((entry.read_bytes(), entry.stat().st_mtime_ns), original)

    def test_conflict_preflights_entire_batch(self):
        target = self.dest / NAMES[-1]
        target.mkdir(parents=True)
        private = target / "my-notes.md"
        private.write_text("personal modifications", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.install()
        self.assertEqual(list(self.dest.iterdir()), [target])
        self.assertEqual(private.read_text(encoding='utf-8'), "personal modifications")

    def test_language_change_requires_preserving_existing_install(self):
        self.install()
        before = {p.relative_to(self.dest): p.read_bytes() for p in self.dest.rglob("*") if p.is_file()}
        with self.assertRaises(ValueError):
            self.install(lang="en")
        after = {p.relative_to(self.dest): p.read_bytes() for p in self.dest.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_dry_run_also_detects_conflict(self):
        self.dest.mkdir()
        (self.dest / NAMES[0]).write_text("existing file", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.install(dry_run=True)
        self.assertEqual((self.dest / NAMES[0]).read_text(encoding='utf-8'), "existing file")

    def test_source_root_is_not_modified(self):
        with self.assertRaises(ValueError):
            installer.install([ROOT / "skills"], NAMES)

    def test_duplicate_destination_is_deduplicated(self):
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install([self.dest, self.dest], NAMES)
        self.assertEqual(len(list(self.dest.iterdir())), len(NAMES))

    def test_skill_symlink_never_overwrites_linked_data(self):
        outside = self.base / "outside"
        outside.mkdir()
        (outside / "note").write_text("preserve", encoding="utf-8")
        self.dest.mkdir()
        try:
            (self.dest / NAMES[0]).symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("Symlinks unavailable on this host")
        with self.assertRaises(ValueError):
            self.install()
        self.assertEqual((outside / "note").read_text(encoding='utf-8'), "preserve")

    def test_write_failure_rolls_back_new_skills(self):
        original_move = installer.shutil.move
        count = 0

        def fail_midway(*args, **kwargs):
            nonlocal count
            count += 1
            if count == 8:
                raise OSError("simulated write failure")
            return original_move(*args, **kwargs)

        with patch.object(installer.shutil, "move", side_effect=fail_midway):
            with self.assertRaises(OSError):
                self.install()
        self.assertEqual(list(self.dest.iterdir()), [])

    def test_all_documented_project_adapters(self):
        for agent, paths in installer.AGENTS.items():
            project = self.base / agent
            result = self.cli("--agent", agent, "--project", str(project), "--skill", "sungemode")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((project / paths[0] / "sungemode/SKILL.md").is_file())

    def test_user_adapters_use_user_home_without_touching_real_home(self):
        with patch.object(installer.Path, "home", return_value=self.base):
            for agent, paths in installer.AGENTS.items():
                with contextlib.redirect_stdout(io.StringIO()):
                    result = installer.main(["--agent", agent, "--scope", "user", "--skill", "sungemode"])
                self.assertEqual(result, 0)
                self.assertTrue((self.base / paths[1] / "sungemode/SKILL.md").is_file())

    def test_custom_target_with_spaces_and_english(self):
        target = self.base / "my agent skills"
        result = self.cli("--dest", str(target), "--lang", "en", "--skill", "sungemode-scout")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(list(target.iterdir())), 1)
        self.assertEqual((target / "sungemode-scout/SKILL.md").read_bytes(), (ROOT / "skills/sungemode-scout/SKILL.en.md").read_bytes())

    def test_unknown_skill_cannot_escape_destination(self):
        result = self.cli("--dest", str(self.dest), "--skill", "../../escape")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.dest.exists())

    def test_target_choice_is_unambiguous(self):
        result = self.cli("--dest", str(self.dest), "--agent", "codex")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.dest.exists())

    def test_all_behavioral_scenarios_reference_shipped_skills(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text(encoding='utf-8'))
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        for case in cases:
            self.assertIn(case["skill"], NAMES)
            self.assertTrue(case["prompt"])
            self.assertTrue(case["expectations"])


if __name__ == "__main__":
    unittest.main()
