---
name: "sungemode-experiment"
description: "Design a small validation experiment within time and budget constraints, defaulting to a seven-day plan with a primary metric and continue/stop thresholds before building or scaling. 孙哥模式行动实验。"
license: "MIT"
---

# Action experiment

Default to English; honor explicit language preferences. Test an assumption that changes a decision; development effort is not validation. This skill stands alone.

## Method

1. Read the opportunity judgment and evidence, or extract the assumption, customer, and constraints from the request. Establish available time, cash cap, recruitable participants, and intended decision. Ask up to three pivotal questions together. Unknown constraints call for conditional plans, not invented budgets.
2. Choose one critical assumption and express it as a falsifiable H proposition. Distinguish pain, willingness to pay, acquisition, and delivery. Prioritize one question per experiment.
3. Select interviews, sample trials, manual delivery, purchase commitments, or another minimal test suited to that assumption. Payment assumptions require observed payment or credible purchase commitments; likes, traffic, and praise are weak evidence. Contacting people, accepting money, or making external commitments must stay within actual authorization; planned actions are not completed results.
4. Default to seven days, honoring a user-specified period. Specify each day's action, output, owner, time, and cash cost, with a fallback for failed recruitment. Sum preparation, recruiting, delivery, and review; stay inside caps.
5. Before execution, set one primary metric, numerator/denominator, recruitment method, continue/adjust/stop thresholds, and observation date. Label thresholds as agreed rules. Insufficient samples warrant insufficient evidence, not manufactured conversion rates or statistical significance.
6. Provide a results table and review questions. Observations are pending until supplied. Supporting metrics explain but never replace the primary metric. Without a reachable channel, test acquisition first rather than promising sales within seven days.

## Output and records

Use [the experiment template](assets/experiment.en.md) for the assumption, design, daily actions, total budget, thresholds, and observed results. Stop conditions include metric failure and time/spending caps. End with one action to begin today.

When asked to save/update, write `.sungemode/projects/<project-slug>/experiment.md` or the chosen path, updating an existing index. Read the previous experiment, preserve its thresholds and version, and record changes in a new experiment rather than redefining success after failure.

