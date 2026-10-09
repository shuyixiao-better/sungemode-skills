<div align="center">

# SungeMode

**Switch your AI into SungeMode.**

Seven interview-inspired themes for work, wealth, health, learning, choices, relationships, and creation.

[中文（default）](README.md) · [English](README.en.md)

![License: MIT](https://img.shields.io/badge/license-MIT-111827)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-2563eb)
![Language](https://img.shields.io/badge/language-中文%20%7C%20English-16a34a)

**Review your context → Make tradeoffs → Act within limits → Update from feedback**

Independently organized and developed by the creator; an unofficial project.

X / Twitter: [@xiao_yi76771](https://x.com/xiao_yi76771) · [@ziguai20](https://x.com/ziguai20)

</div>

Plan across beliefs, decisions, AI learning, business, wealth, health, and life experiences with evidence and shared time/spending limits. Use a whole-life baseline, a specific question, or a periodic review. Existing startup, side-business, and seven-day validation workflows remain available. Portable Markdown records let another agent continue.

Inspired by Alan Shao's public interview with Justin Sun. Interview ideas, our product design, and market claims requiring verification are distinguished in [sources and methodology](docs/sources.en.md).

## Ideas behind the project

SungeMode turns seven interview-inspired ideas into methods for personal choices, action, and review:

- **Scout the map:** Understand options and critical unknowns before acting blindly.
- **AI:** Expand information-processing capacity for organizing context, comparing paths, and learning.
- **Independent judgment (“黄毛理论”):** Distinguish useful criticism from unhelpful social pressure, preserving judgments with evidence.
- **Follow opportunities (“逐水草而居”):** Keep room to change direction as conditions change, accounting for stability and moving costs.
- **Health management:** Protect the body and recovery so long-term action remains sustainable.
- **Financial freedom:** Expand personal choice so time and everyday decisions can better reflect one's priorities.
- **Experience:** Accept that the whole world cannot be understood in advance; learn about oneself and the world through experience and feedback.

Apply these ideas to a whole-life baseline, career/project choices, learning, routines, financial goals, relationships, and creation. The skill translates them into concrete questions, affordable next steps, and review conditions; users need not master the terminology first.

## Try a prompt

```text
Use SungeMode for a whole-life baseline. I have five years of development
experience, want to explore an AI side business and improve my learning,
and want to preserve relationships and rest. After existing obligations,
I have seven hours weekly and a CNY 200 trial budget. I do not want to quit.
Cover all seven themes, keep gaps unknown, and ask at most three key questions.
All actions must share those seven hours and CNY 200. Please answer in English.
```

Expect seven-theme context/gaps, cross-domain tradeoffs, priorities, combined time/cash, and review conditions. Financial and health summaries or ranges suffice; complete private data is not required. A specific question need not trigger a whole-life report.

See the [life baseline demo](examples/life-baseline.en.md), [Chinese equivalent](examples/life-baseline.zh-CN.md), or the existing [project validation demo](examples/seven-day-plan.en.md). These are fictional examples, not completed behavioral evaluations, research, or sales.

## Seven themes and three planning entries

| Theme | Application |
|---|---|
| Cognition | Old assumptions, criticism, path dependence, counterevidence |
| Decisions | Career, location, project choices; scout before committing |
| AI and knowledge | Portable context, learning, verification |
| Business | Demand, global markets, digital IP, technology opportunities |
| Wealth | Cash flow, goals, optionality, stability |
| Health | Habits, records, sustainable observation and adjustment |
| Experience | Relationships, experiences, works, rest |

- **Whole-life baseline:** Assess all seven themes and choose current priorities.
- **Specific question:** Compare a relocation, income, family, and routine tradeoff.
- **Periodic review:** Update the next steps from actual records.

Interview Q&A is also supported. The skill distinguishes personal accounts and universal facts, does not impersonate the guest, equate opposition with truth, or copy his Crypto allocation/health practices. Source notes and limitations are packaged with the main skill for offline reading.

## How the methods change decisions

| Situation | Method | Result |
|---|---|---|
| Persisting despite criticism | Independent judgment | Separate emotion, testable objections, responsibility conflicts; conditional persistence |
| Fragmented learning/context | AI in practice | Minimal portable context and observable learning artifacts |
| Changing environment | Follow opportunities | Compare switching conditions, costs, responsibilities, and stability |
| Career/location/project commitment | Scout first | Investigate a ranking-changing unknown before the next commitment |
| Good income but overload | Body maintenance | Inspect routine/recovery conflicts and reduce tasks rather than keep adding |
| After a wealth milestone | Player mindset | Sample preferences, try a reversible side quest, reflect before deepening |
| More money expected to fix life | Wealth as an amplifier | Locate money-sensitive parts and other necessary agreements/actions |

Names correspond to questions, choices, and feedback. Users need not study the interview first; detailed methods ship with the skill and all seven themes remain covered.

## Five standalone skills

| Skill | Job | Example request |
|---|---|---|
| [`sungemode`](skills/sungemode/SKILL.en.md) | Seven-theme life planning plus existing project workflow | “Help me decide what to do next” |
| [`sungemode-profile`](skills/sungemode-profile/SKILL.en.md) | Goals, capabilities, resources, life constraints | “Create a portable baseline” |
| [`sungemode-scout`](skills/sungemode-scout/SKILL.en.md) | Customers, alternatives, channels, costs | “Map this project opportunity” |
| [`sungemode-experiment`](skills/sungemode-experiment/SKILL.en.md) | Assumption, budget, metric, stop conditions | “Design a seven-day validation test” |
| [`sungemode-review`](skills/sungemode-review/SKILL.en.md) | Review life or project observations against the plan | “Update the plan from this week's results” |

Each skill works independently. `sungemode` contains all seven themes and the full project workflow and does not require the other four; install only what you need to reduce overlapping discovery.

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
├── life.md
├── reviews/2026-10-09.md
└── projects/my-project/
    ├── opportunity.md
    ├── experiment.md
    └── reviews/2026-10-09.md
```

In another tool, ask it to read the index and relevant records and continue the current plan. Whole-life and project reviews are stored separately; existing project records need no migration. Records belong in your working project, separate from installed skills. This repository ignores its own `.sungemode/`; configure your target project's ignore rules as needed for private records.

## Layout and validation

Each `skills/<name>/` contains Chinese `SKILL.md`, English `SKILL.en.md`, bilingual Codex metadata, and output templates. The full entry also includes evidence, source notes, and seven thematic references. Installation/check scripts live in `scripts/`, life and project demos in `examples/`, behavioral scenarios in `evals/`, and installer tests in `tests/`.

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Checks cover both entry languages, metadata, relative resources, language selection, repeat installs, and conflict protection. GitHub Actions defines macOS/Linux/Windows checks on Python 3.9/3.13; remote results depend on actual CI execution. Evaluate skill decisions using [the evaluation guide](evals/README.en.md); structural checks do not prove model performance.

Evaluate practical benefit against direct prompting using the [paired evaluation protocol](evals/comparison.en.md) with matched models/scenarios. The paired comparison is not yet executed; demos and structural tests do not establish effectiveness.

## Connect and share

If SungeMode helps you, star the project or share your use cases, practice notes, and suggestions on X / Twitter. Follow [@xiao_yi76771](https://x.com/xiao_yi76771) and [@ziguai20](https://x.com/ziguai20), and feel free to tag either account when sharing how you turn ideas from the interview into concrete actions.

Contributions are welcome: see [the contribution guide](CONTRIBUTING.en.md). Code and original documentation use the [MIT License](LICENSE); interview and third-party content retain their owners' rights.
