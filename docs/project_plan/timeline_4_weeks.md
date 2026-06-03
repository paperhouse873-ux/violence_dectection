# Four-Week Project Timeline

The combined timeline and research-question PDF is stored as:

```text
docs/project_plan/timeline_and_research_questions.pdf
```

| Week | Focus | Tasks | Deliverables | Evidence |
| --- | --- | --- | --- | --- |
| Week 1 | Literature + Dataset | Read 5 papers, confirm RQs, download RWF-2000/RLVS, run structure/integrity/statistics checks | Literature matrix, dataset protocol, approved RQs | `docs/research/*`, `reports/dataset/*` |
| Week 2 | Baseline | Create split, test DataLoader, fine-tune X3D-S, record E0 baseline | X3D-S checkpoint and E0 metrics | `data/processed/splits/*`, `outputs/results/E0_baseline.json` |
| Week 3 | Context Features + CGM | Extract p_base/crowd/light/motion, train CGM, run E1-E5 ablation | Context cache, ablation table | `outputs/cache/*`, `outputs/results/ablation_table.csv` |
| Week 4 | Validation + Report | Compare models, interpret alpha/feature contribution, prepare thesis evidence | Final result table, figures, written discussion | `outputs/results/phase5_table.csv`, `reports/figures/*` |

## Milestones

- M1: Dataset is valid and reproducible split is committed.
- M2: Baseline X3D-S E0 result is recorded.
- M3: CGM ablation answers RQ1-RQ3.
- M4: Final report has tables, figures, and audit trail.
