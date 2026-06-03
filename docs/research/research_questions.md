# Research Questions

## Core RQs

| RQ | Question | Primary Metric | Evidence Source |
| --- | --- | --- | --- |
| RQ1 | Does CGM reduce false positives compared with X3D-S baseline? | FPR delta E0 -> E4 | `outputs/results/ablation_results.json` |
| RQ2 | Does FPR reduction create an unacceptable false-negative trade-off? | FNR delta E0 -> E4 | `outputs/results/ablation_results.json` |
| RQ3 | Which context stream contributes most to the final prediction? | E1/E2/E3/E4 ablation | `outputs/results/ablation_table.csv` |

## Optional RQ

| RQ | Question | Primary Metric | Evidence Source |
| --- | --- | --- | --- |
| RQ4 | Is motion synchrony redundant when crowd and lighting features are present? | E4 vs variants without motion | Ablation extension |

## Acceptance Notes

- RQ1 is the main thesis claim.
- RQ2 prevents over-optimizing only for FPR.
- RQ3 provides explainability for feature contribution.
- RQ4 can be kept as an extension if advisor asks for exactly 3 approved RQs.

## Source Artifact

The combined timeline and research-question PDF is stored at:

```text
docs/project_plan/timeline_and_research_questions.pdf
```
