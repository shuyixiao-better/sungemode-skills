<div align="center">

# SungeMode｜孙哥模式

**给你的 AI，装上「孙哥模式」。**

从个人现状到机会开图，再到行动与复盘的 AI 技能包。

[中文（默认）](README.md) · [English](README.en.md)

![License: MIT](https://img.shields.io/badge/license-MIT-111827)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-2563eb)
![Language](https://img.shields.io/badge/language-中文%20%7C%20English-16a34a)

**了解你 → 机会开图 → 关键假设 → 小规模验证 → 持续复盘**

Built by Owen

</div>

把一个模糊的项目想法，拆成一份有证据、有预算、有停止条件的七天验证计划。适用于创业、副业、产品探索和职业方向选择；使用 Markdown 保存上下文，让不同 Agent 能接着做。

受邵艾伦 × 孙宇晨公开访谈启发，由 Owen 独立整理与开发，非官方项目。访谈观点、产品化设计与需要查证的市场事实分别标明，详见 [来源与方法](docs/sources.md)。

## 先看一个用法

```text
开启孙哥模式。我会 Java 和 AI 应用开发，每天能投入两小时，
这周预算上限 300 元，可以接触到几位小店主，想做副业。
帮我比较可行方向，给出有证据、有预算和停止条件的七天验证计划。
没有查到的市场信息请标为待验证。请把记录保存在 .sungemode/。
```

你会得到现状与约束、机会比较、关键假设、逐日验证计划、继续/停止条件和复盘入口。当前市场事实需要 Agent 用实际可用的浏览工具查证；没有联网能力也能生成明确标注为待验证的方案。

查看 [完整中文演示](examples/seven-day-plan.zh-CN.md) / [English demo](examples/seven-day-plan.en.md)。示例使用虚构场景，展示输出结构；其中的假设、数字和计划不代表真实研究或成交。

## 五个技能

| 技能 | 用途 | 典型指令 |
|---|---|---|
| [`sungemode`](skills/sungemode/SKILL.md) | 完整闭环，一个入口即可 | “开启孙哥模式，帮我判断下一步做什么” |
| [`sungemode-profile`](skills/sungemode-profile/SKILL.md) | 个人档案：目标、能力、资源与约束 | “整理我的现状，建立可移交的档案” |
| [`sungemode-scout`](skills/sungemode-scout/SKILL.md) | 机会开图：客户、替代、渠道与成本 | “给这个项目想法开图” |
| [`sungemode-experiment`](skills/sungemode-experiment/SKILL.md) | 行动实验：假设、预算、指标与停止条件 | “设计一个七天最小验证” |
| [`sungemode-review`](skills/sungemode-review/SKILL.md) | 复盘：计划对照实际，更新判断 | “根据这周的结果调整下一步” |

每个技能可以独立安装和使用。`sungemode` 自身包含完整流程，不依赖其他四个技能；按需安装可减少技能列表的重复匹配。

## 安装

需要 Python 3.9+。安装脚本只用标准库，不下载依赖、不要求 API Key。macOS/Linux 使用 `python3`；Windows 可使用 `py -3` 替换。

```bash
git clone https://github.com/shuyixiao-better/sungemode-skills.git
cd sungemode-skills

# 查看技能；预览安装，不写文件
python3 scripts/install.py --list
python3 scripts/install.py --agent codex --scope user --dry-run

# 给 Codex 安装，默认中文；在所有本地项目中使用
python3 scripts/install.py --agent codex --scope user

# Claude Code / Qoder（按需选一条）
python3 scripts/install.py --agent claude-code --scope user
python3 scripts/install.py --agent qoder --scope user

# 仅安装完整入口到指定项目，也可以重复 --agent 同时安装到多个工具
python3 scripts/install.py --agent codex --agent claude-code --scope project --project /path/to/your-project --skill sungemode

# 安装完整英文入口（在另一个项目中示范）
python3 scripts/install.py --agent cursor --scope project --project /path/to/english-project --lang en
```

`--scope` 默认是 `project`，项目路径默认为运行命令时的目录；给其他项目安装时使用 `--project`。若想所有项目通用，明确使用 `--scope user`。可重复 `--skill` 选择多个技能。

安装后新开会话或按工具提供的方式刷新技能，确认技能列表里出现 `sungemode`。Codex 可以用 `$sungemode`；Claude Code 和 Qoder 可以用 `/sungemode`。也可以直接说“开启孙哥模式”。具体安装位置、调用差异及官方依据见 [工具兼容说明](docs/compatibility.md)。

### 支持哪些工具

安装器包含 Codex、Claude Code、Qoder、Cursor、GitHub Copilot、Gemini CLI 和 OpenCode 的官方目录规则。技能采用 [Agent Skills 标准](https://agentskills.io/specification)，不依赖某个厂商的专用运行工具。目录与格式适配经过本地测试；各产品的实际加载和模型表现需在对应版本中验证。

其他支持 `SKILL.md` 的工具可以指定目录：

```bash
python3 scripts/install.py --dest /path/to/agent/skills --skill sungemode
```

### 中英文如何切换

- 默认安装 `SKILL.md` 中文入口和中文 Codex 界面元数据，输出默认简体中文。
- `--lang en` 将 `SKILL.en.md` 作为安装后的 `SKILL.md`，并选用英文界面元数据；英文安装默认英文。
- 两种安装都保留中英文模板和参考资料，文件名、技能名与记录路径一致。
- 用户在对话中明确说“请用英文回答”或“请用中文回答”，技能遵从该偏好，无需重新安装。

### 已有安装、升级与卸载

相同内容重复安装会跳过；存在不同内容时整批安装在写入前拒绝，保护已有修改。切换安装语言或升级时，先把目标的 `sungemode*` 技能目录移到技能搜索目录之外的备份位置，再安装；备份保留原文件，失败时可移回。卸载只需移走对应技能目录，个人记录独立保存。

## 用 Markdown 让不同 Agent 接着做

需要保存时告诉 Agent “把记录保存在 `.sungemode/`”。单纯咨询默认在对话交付，不自动建立个人记录。

```text
.sungemode/
├── README.md
├── profile.md
└── projects/my-project/
    ├── opportunity.md
    ├── experiment.md
    └── reviews/2026-10-09.md
```

换工具后可以说：“读取 `.sungemode/README.md` 和相关记录，继续当前实验。”记录放在工作项目，技能文件放在工具目录。仓库的 `.gitignore` 忽略自身的 `.sungemode/`；在其他项目保存私人记录时按需要配置该项目的忽略规则。

## 项目结构与验证

```text
skills/<name>/
├── SKILL.md                # 默认中文入口
├── SKILL.en.md             # 完整英文入口
├── agents/openai*.yaml     # Codex 中英文界面元数据
├── assets/                 # 中英文输出模板
└── references/             # 按需加载的参考（完整入口）
scripts/                    # 安装与检查
examples/                   # 中英文七天验证演示
evals/                      # 真实使用场景与人工评估标准
tests/                      # 安装行为测试
docs/                       # 兼容与来源说明
```

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

检查覆盖中英文入口、元数据、相对资源链接、安装语言、重复安装与冲突保护。GitHub Actions 配置了 macOS/Linux/Windows、Python 3.9/3.13 的检查矩阵；远程 CI 状态以实际运行结果为准。Skill 的决策表现按 [评估说明](evals/README.md) 验证，结构检查不能替代实际使用。

欢迎贡献新的证据规则、实际案例或工具适配。请先读 [贡献指南](CONTRIBUTING.md)。项目代码和原创文档使用 [MIT License](LICENSE)；公开访谈及第三方内容的权利属于其原作者。

