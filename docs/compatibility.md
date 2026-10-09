# 工具兼容与安装位置

核对日期：2026-10-09。以下是官方文档记载的安装路径，安装脚本据此适配；实际界面、加载优先级与功能以各工具当前版本为准。

| `--agent` | 项目级 | 用户级 | 官方依据 |
|---|---|---|---|
| `codex` | `.agents/skills/` | `~/.agents/skills/` | [Codex skills](https://learn.chatgpt.com/docs/build-skills) |
| `claude-code` | `.claude/skills/` | `~/.claude/skills/` | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| `qoder` | `.qoder/skills/` | `~/.qoder/skills/` | [Qoder IDE](https://docs.qoder.com/extensions/skills)、[Qoder CLI](https://docs.qoder.com/cli/Skills) |
| `cursor` | `.cursor/skills/` | `~/.cursor/skills/` | [Cursor skills](https://cursor.com/docs/skills) |
| `copilot` | `.github/skills/` | `~/.copilot/skills/` | [Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) |
| `gemini` | `.gemini/skills/` | `~/.gemini/skills/` | [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) |
| `opencode` | `.opencode/skills/` | `~/.config/opencode/skills/` | [OpenCode skills](https://opencode.ai/docs/skills/) |

`--scope user` 安装到本机用户目录。远程/云端 Agent 未必可访问本机目录；这类环境需要把技能放入它实际读取的项目或工作区，再按相应产品流程启用。

## 发现与调用

- Codex：在新会话确认技能可用，使用 `$sungemode` 或自然语言请求。
- Claude Code：新会话查看 `/` 菜单，可使用 `/sungemode`。
- Qoder IDE：重启后查看 `/` 列表；Qoder CLI 可使用 `/skills reload`，然后 `/sungemode`。
- Cursor：确认 Agent 技能列表，按界面提供的技能选择入口调用。
- Gemini CLI：用 `/skills list` 查看，必要时 `/skills reload`；通过任务描述调用。
- Copilot / OpenCode：确认当前环境支持并启用技能，通过任务描述调用；OpenCode 还受技能权限配置影响。

Qoder IDE 与 CLI 文档对同名技能的优先级描述不同；不要依靠覆盖优先级切换语言，保持每种工具只有一个有效安装。Codex 的 `.agents/skills/` 也可能被其他兼容工具读取，安装时避免多个目录中的同名重复版本。

## 标准与能力边界

所有技能遵循 [Agent Skills 目录和 frontmatter 格式](https://agentskills.io/specification)，只使用 `name`、`description`、`license` 公共字段。`agents/openai.yaml` 是 Codex 界面元数据，其他工具可忽略。安装脚本将选定语言入口写为标准 `SKILL.md`，参考资料和模板随技能一起复制，相对路径不指向原仓库。

技能不自带联网、模型服务、联系人系统或支付能力。查证与执行使用宿主已经提供并允许使用的工具；无浏览工具时标记未知并生成验证清单。安装检查只证明包结构和文件适配，不证明每个产品版本中的自动触发或分析质量。

没有原生 Skills 支持的 Agent，可以在任务中明确让它读取仓库的 `skills/sungemode/SKILL.md`（或英文 `SKILL.en.md`）及相关资源；这是手动读取方式，不应宣传为自动发现支持。

