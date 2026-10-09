# Compatibility and installation paths

Checked on 2026-10-09. Paths below are documented by the vendors and used by the installer. UI, precedence, and supported features depend on the product/version.

| `--agent` | Project | User | Official source |
|---|---|---|---|
| `codex` | `.agents/skills/` | `~/.agents/skills/` | [Codex skills](https://learn.chatgpt.com/docs/build-skills) |
| `claude-code` | `.claude/skills/` | `~/.claude/skills/` | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| `qoder` | `.qoder/skills/` | `~/.qoder/skills/` | [Qoder IDE](https://docs.qoder.com/extensions/skills), [CLI](https://docs.qoder.com/cli/Skills) |
| `cursor` | `.cursor/skills/` | `~/.cursor/skills/` | [Cursor skills](https://cursor.com/docs/skills) |
| `copilot` | `.github/skills/` | `~/.copilot/skills/` | [Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) |
| `gemini` | `.gemini/skills/` | `~/.gemini/skills/` | [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) |
| `opencode` | `.opencode/skills/` | `~/.config/opencode/skills/` | [OpenCode skills](https://opencode.ai/docs/skills/) |

User scope installs on this machine. Cloud/remote agents may not read local user directories; place skills in their actual project/workspace and follow the product's enablement flow.

## Discovery and invocation

- Codex: confirm discovery in a fresh session, then use `$sungemode` or a natural-language request.
- Claude Code: inspect the `/` menu in a new session and invoke `/sungemode`.
- Qoder IDE: restart and inspect the `/` list. Qoder CLI supports `/skills reload`, then `/sungemode`.
- Cursor: confirm the Agent skill list and use the offered selection UI.
- Gemini CLI: inspect `/skills list`, refresh with `/skills reload` if needed, then describe the task.
- Copilot/OpenCode: confirm skills are supported/enabled in the environment, then describe the task. OpenCode skill permissions also apply.

Qoder IDE and CLI documentation differ on same-name precedence; keep one active version rather than relying on precedence for language switching. Other compatible tools may read Codex's `.agents/skills/`; avoid duplicate names with different contents.

## Format and limits

Skills follow the [Agent Skills specification](https://agentskills.io/specification), using the common `name`, `description`, and `license` fields. `agents/openai.yaml` is Codex UI metadata and can be ignored elsewhere. The installer promotes the selected language to `SKILL.md` and copies local templates/references, with no dependency on the original repository.

Skills do not supply browsing, model services, contacts, or payment systems. They use tools already available and authorized in the host. Without browsing, unknowns stay explicit. Package checks establish structure and installation behavior, not successful triggering or analysis quality in every product/version.

For agents without native Skills support, explicitly ask them to read `skills/sungemode/SKILL.md` or `SKILL.en.md` and the referenced resources. This is manual loading, not automatic discovery support.

