# Data Directory

Dataset video files are intentionally ignored by Git.

Expected layout:

```text
data/raw/RWF-2000/
├── train/fight/
├── train/nonFight/
├── val/fight/
└── val/nonFight/

data/raw/RLVS/
```

Commit reproducible metadata only, such as split files in `data/processed/splits/`.
