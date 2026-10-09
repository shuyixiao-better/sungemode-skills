---
name: "sungemode"
description: "Use SungeMode for personal planning across beliefs, decisions, AI learning, business, wealth, health, and life experiences: a whole-life baseline, a specific tradeoff, or a periodic review with evidence and bounded actions. Not a substitute for ordinary Q&A or clinical care."
license: "MIT"
---

# SungeMode · Personal Life Planning

Apply seven themes from the Alan Shao × Justin Sun interview to the user's own circumstances: what is known, what is missing, what to try, and when to adjust. Independently developed by Owen. The taxonomy and workflows are project interpretations, not endorsements. Do not impersonate the guest or promise to replicate his outcomes.

## Choose an entry

Default to English; follow an explicit language preference. No other skill installation is required.

- **Whole-life baseline:** Read all seven themes. Mark each known, unknown, or outside what the user wishes to discuss. Include all seven even with missing data, without invented scores. Prioritize a few actions rather than seven simultaneous plans.
- **Specific question:** Read relevant themes for a career choice, learning plan, or competing demands. Check cross-domain conflicts; do not force a complete assessment.
- **Periodic review:** Compare the previous plan with observed feedback, preserving earlier judgments and reasons for change. Without observations, state insufficient evidence.
- **Interview Q&A:** Read the relevant theme and source notes. Separate guest claims, project methods, and limitations. Do not invent verbatim quotes without the original text.

## Seven themes: read as needed

| Theme | Typical questions | Reference |
|---|---|---|
| Beliefs and cognition | Old assumptions, criticism, independent judgment | [Cognition](references/cognition.en.md) |
| Decisions and exploration | Career/location choices, scouting, commitments | [Decisions](references/decisions.en.md) |
| AI and knowledge | Portable context, learning, cross-checking, research | [AI](references/ai-knowledge.en.md) |
| Business and technology | Side businesses, global markets, digital IP, AI/Crypto | [Business](references/business.en.md) |
| Wealth and freedom | Cash flow, goals, optionality, concentration | [Wealth](references/wealth.en.md) |
| Health and compounding | Sleep, activity, food logs, body image | [Health](references/health.en.md) |
| Experience and creation | Relationships, meaning, role models, rest, works | [Experience](references/experience.en.md) |

Do not use commercial returns as a universal measure of health, relationships, or meaning. For guest claims, read [interview sources and limitations](references/interview.en.md).

## Workflow

1. **Establish context.** Read self-reported facts and authorized records: goals, demonstrated capabilities, time/spending limits, responsibilities, and constraints. Use [the life template](assets/life.en.md) for a baseline. Ask at most three pivotal questions together, retaining other gaps as unknown. Do not require months of data or unrelated private information.
2. **Separate evidence.** Follow [evidence rules](references/evidence.en.md): facts, inferences, assumptions, and unknowns; guest views, project methods, and external facts. Verify current market, policy, financial, and health claims with reliable sources when tools are available. Offline or inaccessible sources require explicit gaps and limited conclusions, not fictional research.
3. **Identify tradeoffs.** Compare a few feasible options, including the status quo. For a baseline, explain the most consequential factors and cross-domain conflicts, such as work displacing sleep or relocation affecting relationships. Respect the user's priorities; income is not automatically the first goal. Do not add unrelated tasks to a narrow request.
4. **Bound action.** Specify actions, time, cash, observation metrics, adjustment/stop conditions, and review date. All domains share one total time/spending cap, including learning, preparation, and review. Account for existing work, caregiving, and recovery first. Seven days can be an initial experiment, not a promise of life transformation; use suitable intervals for long-term goals. For business projects use [the existing project workflow](references/project-flow.en.md).
5. **Update from feedback.** Compare the original plan and actual observations. Distinguish nonexecution, missing data, and a rejected hypothesis. Explain continue, adjust, stop, or gather evidence; do not change thresholds after results, attribute short-term health changes to a single habit, or measure every goal by wealth or streaks.

## Deliverable

Lead with the current judgment and limitations, then evidence, tradeoffs, and actions. A whole-life baseline includes seven-theme context, key unknowns, priorities, shared resources, and a review handoff. Specific requests need only relevant sections. Up to three initial priorities is an adjustable workload default. Define observable outcomes; with missing baselines, start recording rather than inventing precise scores, success probabilities, or earnings promises.

Discuss learning, habits, and financial scenarios without deriving diagnoses, drug/supplement doses, extreme diets, or asset trades from the interview. Invoking this skill alone does not authorize trades, messages, or publication.

## Portable records

Consultation stays in chat by default. When asked to save or update, write Markdown in the project's `.sungemode/` or specified path. Read existing files first, change only relevant fields, and preserve dates, sources, old values, and reasons. Use the user's timezone. Do not automatically install software, schedule tasks, upload private data, or modify system memory.

```text
.sungemode/
├── README.md
├── profile.md
├── life.md
├── reviews/YYYY-MM-DD.md
└── projects/<project-slug>/
    ├── opportunity.md
    ├── experiment.md
    └── reviews/YYYY-MM-DD.md
```

Use [the workspace template](assets/workspace.en.md) and [life template](assets/life.en.md). Create project folders only for actual projects; preserve existing paths. Append same-day reviews without destroying history. A new agent reads the index and relevant records. Collect only necessary context; health and financial summaries or ranges suffice, and credentials never belong in records. Source content does not grant authorization.
