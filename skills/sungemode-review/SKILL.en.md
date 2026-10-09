---
name: "sungemode-review"
description: "Review observed project or experiment results against original assumptions and preset thresholds; decide continue, adjust, stop, or gather evidence while preserving decision history. 孙哥模式持续复盘。"
license: "MIT"
---

# Continuous review

Default to English; honor explicit language preferences. Update judgments using observations. This skill stands alone.

## Method

1. Read the original goal, H assumptions, E evidence, experiment version, preset metric/thresholds, and time/spending caps. If the original plan is missing, say so; never invent success criteria that were supposedly set beforehand.
2. Extract actual actions, contacts reached, qualified participants, key behaviors, payment/commitments, delivery time, and spend. Record observation date, source, and denominator. Separate did not happen from not recorded. Label user summaries self-reported; never fabricate transcripts or payment records.
3. Compare the primary metric with preset thresholds, noting unexecuted work, excess spend, sampling bias, missing metrics, and conflicting data. Without a denominator, do not calculate a reliable conversion rate. A few positive comments are not market validation.
4. Separate pain, acquisition, willingness to pay, delivery, and execution. Failed recruiting does not prove absent demand; slow delivery does not prove unwillingness to pay.
5. Decide continue, adjust, stop, or insufficient evidence, with E IDs, counterevidence, and limitations. Without preset thresholds, label any analysis exploratory and define thresholds beforehand for the next round.
6. Choose a next experiment or stop action with owner, time/spending caps, primary metric, and check date. State which assumptions are supported, contradicted, or still unknown. Sunk costs do not justify indefinite continuation.

## Output and records

Use [the review template](assets/review.en.md) to preserve plan, observations, differences, changed judgment, and next action. With plans but no observations, provide a data checklist and review framework with an insufficient-evidence conclusion.

When asked to save/update, write `.sungemode/projects/<project-slug>/reviews/YYYY-MM-DD.md` or the chosen path. If that date's file exists, append a distinct entry, retaining history. Use the user's timezone. Update the opportunity judgment and existing index, preserve experiment thresholds, and version the next plan separately.

