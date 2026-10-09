<div align="center">

# SungeMode

**Switch your AI into SungeMode.**

Agent skills for personal context, opportunity scouting, action, and review.

[中文（default）](README.md) · [English](README.en.md)

![License: MIT](https://img.shields.io/badge/license-MIT-111827)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-2563eb)
![Language](https://img.shields.io/badge/language-中文%20%7C%20English-16a34a)

**Understand you → Map opportunities → Test assumptions → Review results**

Built by Owen

</div>

Turn a vague project idea into an evidence-based seven-day validation plan with time, budget, and stop conditions. Suitable for startups, side businesses, product exploration, and career choices. Portable Markdown records let another agent continue the work.

Independently developed by Owen, inspired by Alan Shao's public interview with Justin Sun. This is an unofficial project. Interview ideas, our product design, and market claims requiring verification are distinguished in [sources and methodology](docs/sources.en.md).

## Try a prompt

```text
Use SungeMode. I know Java and AI application development, have two hours
per day and a CNY 300 budget this week, and can reach a few local shop owners.
Compare feasible side-project directions. Give me a seven-day test with
evidence, budget, and stop conditions. Label unverified market information.
Please answer in English and save the records in .sungemode/.
```

Expect a baseline, opportunity comparison, critical assumption, daily validation plan, continue/stop rules, and review handoff. Current market facts require the agent's available browsing tools. Without browsing, it can deliver a clearly provisional plan and verification checklist.

See the [English demo](examples/seven-day-plan.en.md) / [Chinese demo](examples/seven-day-plan.zh-CN.md). The scenario and numbers are fictional, illustrating the output rather than completed research or sales.

## Five standalone skills

| Skill | Job | Example request |
|---|---|---|
| [`sungemode`](skills/sungemode/SKILL.en.md) | Full context-to-action loop | “Help me decide what to do next” |
| [`sungemode-profile`](skills/sungemode-profile/SKILL.en.md) | Goals, capabilities, resources, constraints | “Create a portable baseline” |
| [`sungemode-scout`](skills/sungemode-scout/SKILL.en.md) | Customers, alternatives, channels, costs | “Map this project opportunity” |
| [`sungemode-experiment`](skills/sungemode-experiment/SKILL.en.md) | Assumption, budget, metric, stop conditions | “Design a seven-day validation test” |
| [`sungemode-review`](skills/sungemode-review/SKILL.en.md) | Compare observations with the plan | “Update the plan from this week's results” |

Each skill works independently. `sungemode` contains the full workflow and does not require the other four; install only what you need to reduce overlapping discovery.

## Install

Requires Python 3.9+. The installer uses only the standard library, downloads no dependencies, and needs no API key. On Windows, replace `python3` with `py -3`.

```bash
git clone https://github.com/shuyixiao-better/sungemode-skills.git
cd sungemode-skills

python3 scripts/install.py --list
python3 scripts/install.py --agent codex --scope user --dry-run

# Default Chinese installation
python3 scripts/install.py --agent codex --scope user

# English installation; choose the agent you use
python3 scripts/install.py --agent claude-code --scope user --lang en
python3 scripts/install.py --agent qoder --scope user --lang en

# Full entry only, for one project and multiple tools
python3 scripts/install.py --agent codex --agent cursor --scope project --project /path/to/project --skill sungemode --lang en

# Custom skills root for another compatible tool
python3 scripts/install.py --dest /path/to/agent/skills --skill sungemode --lang en
```

Scope defaults to `project`, and the project defaults to the command's current working directory. Use `--project` to target a different project or `--scope user` for local cross-project use. Repeat `--agent` or `--skill` to select multiple targets or skills.

Start a new session or refresh skills, then confirm `sungemode` appears. Codex supports `$sungemode`; Claude Code and Qoder support `/sungemode`. Natural-language requests can also select the skill. See [compatibility and official references](docs/compatibility.en.md).

The installer supports documented paths for Codex, Claude Code, Qoder, Cursor, GitHub Copilot, Gemini CLI, and OpenCode. Skills follow the [Agent Skills standard](https://agentskills.io/specification) without vendor-specific runtime tools. Format and directory adaptation are locally tested; actual discovery and model behavior need verification in each product/version.

### Languages

Chinese is the repository and installation default. `--lang en` promotes `SKILL.en.md` to the installed `SKILL.md` and selects English Codex metadata; that installation defaults to English. Both packages retain bilingual templates and references. Names and record paths stay identical. Explicit conversation-level language requests override the default without reinstalling.

### Existing installations, updates, and removal

Identical installations are skipped. Different existing content blocks the entire batch before writing. For updates or installation-language changes, first move the affected `sungemode*` directories to a backup outside all skill search roots, then install again. Retain backups for rollback. Remove skills by moving their installed directories; personal records live separately.

## Portable records

Ask the agent to save records in `.sungemode/`. Consultation alone returns Markdown in chat without automatically creating personal records.

```text
.sungemode/
├── README.md
├── profile.md
└── projects/my-project/
    ├── opportunity.md
    ├── experiment.md
    └── reviews/2026-10-09.md
```

In another tool, ask it to read the index and relevant records and continue the current experiment. Records belong in your working project, separate from installed skills. This repository ignores its own `.sungemode/`; configure your target project's ignore rules as needed for private records.

## Layout and validation

Each `skills/<name>/` contains Chinese `SKILL.md`, English `SKILL.en.md`, bilingual Codex metadata, and output templates. The full entry also includes evidence references. Installation/check scripts live in `scripts/`, demos in `examples/`, behavioral scenarios in `evals/`, and installer tests in `tests/`.

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Checks cover both entry languages, metadata, relative resources, language selection, repeat installs, and conflict protection. GitHub Actions defines macOS/Linux/Windows checks on Python 3.9/3.13; remote results depend on actual CI execution. Evaluate skill decisions using [the evaluation guide](evals/README.en.md); structural checks do not prove model performance.

Contributions are welcome: see [the contribution guide](CONTRIBUTING.en.md). Code and original documentation use the [MIT License](LICENSE); interview and third-party content retain their owners' rights.
