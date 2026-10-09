#!/usr/bin/env python3
"""Install standalone SungeMode skills with Python's standard library only."""

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"
AGENTS = {
    "codex": (".agents/skills", ".agents/skills"),
    "claude-code": (".claude/skills", ".claude/skills"),
    "qoder": (".qoder/skills", ".qoder/skills"),
    "cursor": (".cursor/skills", ".cursor/skills"),
    "copilot": (".github/skills", ".copilot/skills"),
    "gemini": (".gemini/skills", ".gemini/skills"),
    "opencode": (".opencode/skills", ".config/opencode/skills"),
}


def payload(source, lang):
    """Materialize the chosen entrypoint and keep every relative resource local."""
    files = {}
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"源文件包含符号链接 / Source symlink: {path}")
        if not path.is_file():
            continue
        rel = path.relative_to(source)
        if rel.as_posix() in ("SKILL.md", "SKILL.en.md", "agents/openai.yaml", "agents/openai.en.yaml"):
            continue
        files[rel.as_posix()] = path.read_bytes()
    entry = "SKILL.en.md" if lang == "en" else "SKILL.md"
    ui = "openai.en.yaml" if lang == "en" else "openai.yaml"
    files["SKILL.md"] = (source / entry).read_bytes()
    files["agents/openai.yaml"] = (source / "agents" / ui).read_bytes()
    files["LICENSE"] = (REPO / "LICENSE").read_bytes()
    return files


def existing_payload(target):
    if target.is_symlink() or not target.is_dir():
        return None
    files = {}
    for path in target.rglob("*"):
        if path.is_symlink():
            return None
        if path.is_file():
            files[path.relative_to(target).as_posix()] = path.read_bytes()
    return files


def install(roots, names, lang="zh", dry_run=False):
    """Preflight the entire batch; never replace an existing skill."""
    packages = {name: payload(SKILLS / name, lang) for name in names}
    plan = []
    seen = set()
    for root in roots:
        root = root.expanduser().absolute()
        if root.is_symlink():
            raise ValueError(f"目标目录为符号链接 / Destination symlink: {root}")
        if root.exists() and not root.is_dir():
            raise ValueError(f"目标不是目录 / Not a directory: {root}")
        resolved = root.resolve()
        if resolved == SKILLS.resolve() or SKILLS.resolve() in resolved.parents:
            raise ValueError("不能安装到源码目录 / Cannot install into source skills")
        for name, files in packages.items():
            target = root / name
            identity = target.resolve()
            if identity in seen:
                continue
            seen.add(identity)
            if target.exists() or target.is_symlink():
                if existing_payload(target) != files:
                    raise ValueError(
                        f"已有不同内容，未覆盖 / Existing content differs: {target}\n"
                        "请先把该目录移到备份位置，再重试 / Move it to a backup location before retrying."
                    )
                plan.append((target, files, "skip"))
            else:
                plan.append((target, files, "install"))
    if dry_run:
        for target, _, action in plan:
            print(f"[dry-run:{action}] {target}")
        return
    created = []
    try:
        for target, files, action in plan:
            if action == "skip":
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(prefix=".sungemode-stage-", dir=target.parent) as tmp:
                stage = Path(tmp) / target.name
                stage.mkdir()
                for rel, data in files.items():
                    path = stage / rel
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(data)
                # Reserve our own directory without replacing a concurrent install.
                target.mkdir()
                created.append(target)
                for child in stage.iterdir():
                    shutil.move(str(child), str(target / child.name))
    except OSError:
        for target in reversed(created):
            shutil.rmtree(target)
        raise
    for target, _, action in plan:
        print(f"[{action}] {target}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="安装孙哥模式 / Install SungeMode (Python 3.9+)")
    parser.add_argument("--agent", action="append", choices=sorted(AGENTS), help="可重复 / Repeatable")
    parser.add_argument("--scope", choices=("project", "user"), default="project")
    parser.add_argument("--project", type=Path, default=Path.cwd(), help="项目路径 / Project root")
    parser.add_argument("--dest", type=Path, help="自定义 skills 根目录 / Custom skills root")
    parser.add_argument("--skill", action="append", help="仅安装指定技能，可重复 / Repeatable skill name")
    parser.add_argument("--lang", choices=("zh", "en"), default="zh")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--list", action="store_true", help="列出技能 / List skills")
    args = parser.parse_args(argv)
    available = sorted(p.name for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    if args.list:
        print("\n".join(available))
        return 0
    if bool(args.agent) == bool(args.dest):
        parser.error("请选择 --agent 或 --dest / Choose --agent or --dest")
    names = list(dict.fromkeys(args.skill or available))
    if any(name not in available for name in names):
        parser.error("未知技能 / Unknown skill: " + ", ".join(n for n in names if n not in available))
    if args.dest:
        roots = [args.dest]
    else:
        base = args.project if args.scope == "project" else Path.home()
        index = 0 if args.scope == "project" else 1
        roots = [base / AGENTS[agent][index] for agent in args.agent]
    try:
        install(roots, names, args.lang, args.dry_run)
    except (OSError, ValueError) as exc:
        print(f"安装失败 / Installation failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

