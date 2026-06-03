# Violence Detection Research

This repository contains a video violence detection research project focused on the following pipeline:

1. Validate and standardize the RWF-2000/RLVS datasets.
2. Fine-tune the X3D-S base detector on RWF-2000.
3. Extract context features: crowd, lighting, and motion.
4. Train the Context Gating Module (CGM) and run ablations for FPR/FNR analysis.
5. Compare additional modern detectors such as SwinV2, ConvNeXt, and EfficientNetV2.

## Project Structure

```text
.
├── src/violence_detection/      # Reusable code: datasets, models, and utilities
├── scripts/                     # Experiment phase scripts
├── data/
│   ├── raw/                     # Raw datasets, not committed to Git
│   └── processed/splits/        # Reproducible split JSON files
├── docs/
│   ├── research/                # Paper, literature matrix, research questions
│   ├── datasets/                # Dataset protocol and checklist
│   ├── project_plan/            # Four-week project timeline
│   └── evidence/                # Decision log and AI audit log
├── outputs/                     # Heavy checkpoints, caches, and results
├── reports/                     # Small report artifacts for evidence
└── configs/                     # Experiment configs for future extensions
```

## Environment Setup

Recommended requirements:

- Python 3.10
- PyTorch 2.x
- CUDA matching the available GPU environment
- PyTorchVideo, Ultralytics, OpenCV, scikit-learn, pandas, wandb
- Git and Git LFS if large metadata or special artifacts are needed

Create the environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

Quick check:

```powershell
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

## Dataset Layout

Do not commit video datasets to Git. Place the datasets as follows:

```text
data/raw/RWF-2000/
├── train/fight/
├── train/nonFight/
├── val/fight/
└── val/nonFight/

data/raw/RLVS/
```

The main split file is stored at:

```text
data/processed/splits/rwf2000_split.json
```

## Reproducible Workflow

Run the workflow in order:

```powershell
python scripts/phase0_check_structure.py
python scripts/phase0_check_integrity.py
python scripts/phase0_statistics.py
python scripts/phase0_create_split.py

python scripts/phase1_test_dataloader.py
python scripts/phase2_finetune_x3ds.py --root data/raw/RWF-2000 --split data/processed/splits/rwf2000_split.json
python scripts/phase3_extract_context.py --root data/raw/RWF-2000 --split data/processed/splits/rwf2000_split.json
python scripts/phase4_train_cgm.py
python scripts/phase5_modern_detectors.py --root data/raw/RWF-2000 --split data/processed/splits/rwf2000_split.json
```

## Research Evidence

Recommended files to update before pushing or submitting:

- `docs/research/related_work.pdf`: drafted related work and literature review content.
- `docs/project_plan/timeline_and_research_questions.pdf`: combined timeline and research questions document.
- `docs/research/literature_review_matrix.md`: summary of at least 5 papers.
- `docs/research/research_questions.md`: RQ, metric, hypothesis, evidence.
- `docs/datasets/dataset_protocol.md`: dataset sources, integrity checks, and label mapping.
- `docs/project_plan/timeline_4_weeks.md`: weekly timeline and deliverables.
- `docs/evidence/ai_audit_log.md`: prompt and decision log for AI-assisted work.
- `reports/dataset/`: dataset statistics and issue reports after Phase 0.
