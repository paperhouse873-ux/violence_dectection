"""
Phase 0 — Step 4: Create train/val/test split 70/15/15
=====================================================
Run:
  python scripts/phase0_create_split.py ^
    --root data/raw/RWF-2000 ^
    --out data/processed/splits/rwf2000_split.json ^
    --seed 42

The original RWF-2000 layout only provides train (1600) and val (400).
This script:
  - Merges all 2000 clips
  - Creates a stratified 70/15/15 split (1400/300/300)
  - Saves data/processed/splits/rwf2000_split.json for all experiments

Why split.json matters:
  It ensures every model (M1, M2, M3, M4) trains and tests on the same
  dataset partition. Without it, model comparisons are not fair.
"""

import json
import random
import argparse
from pathlib import Path
from collections import defaultdict

from _bootstrap import PROJECT_ROOT

VIDEO_EXTS = {".avi", ".mp4", ".mov", ".mkv"}

LABEL_MAP = {
    "fight":    1,  # violent
    "nonFight": 0,  # non-violent
}


def collect_clips(root: Path) -> dict[str, list[str]]:
    """Collect clips by label while ignoring the original train/val folders."""
    clips_by_label: dict[str, list[str]] = defaultdict(list)

    for split_dir in ["train", "val"]:
        for label in ["fight", "nonFight"]:
            folder = root / split_dir / label
            if not folder.exists():
                continue
            for f in folder.iterdir():
                if f.suffix.lower() in VIDEO_EXTS:
                    # Store a portable relative path.
                    clips_by_label[label].append(
                        f.relative_to(root).as_posix()
                    )

    return dict(clips_by_label)


def stratified_split(
    clips_by_label: dict[str, list[str]],
    train_ratio: float = 0.70,
    val_ratio:   float = 0.15,
    seed:        int   = 42,
) -> dict:
    """Create a stratified split with the same ratio for each class."""
    rng = random.Random(seed)
    split = {"train": [], "val": [], "test": []}

    for label, clips in clips_by_label.items():
        shuffled = clips[:]
        rng.shuffle(shuffled)

        n  = len(shuffled)
        n_train = int(n * train_ratio)
        n_val   = int(n * val_ratio)

        split["train"] += [{"path": p, "label": LABEL_MAP[label]}
                           for p in shuffled[:n_train]]
        split["val"]   += [{"path": p, "label": LABEL_MAP[label]}
                           for p in shuffled[n_train:n_train + n_val]]
        split["test"]  += [{"path": p, "label": LABEL_MAP[label]}
                           for p in shuffled[n_train + n_val:]]

    # Shuffle again so samples are not grouped by label.
    for s in split:
        rng.shuffle(split[s])

    return split


def print_summary(split: dict):
    print(f"\n{'='*50}")
    print(f"  Split summary (seed=42, stratified)")
    print(f"{'='*50}")
    for name, clips in split.items():
        n_violent     = sum(1 for c in clips if c["label"] == 1)
        n_nonviolent  = sum(1 for c in clips if c["label"] == 0)
        print(f"\n  {name:5s}: {len(clips):4d} clips  "
              f"(violent={n_violent}, non-violent={n_nonviolent})")
    total = sum(len(v) for v in split.values())
    print(f"\n  Total: {total} clips")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root",  type=str,
                        default=str(PROJECT_ROOT / "data" / "raw" / "RWF-2000"))
    parser.add_argument("--out", type=str,
                        default=str(PROJECT_ROOT / "data" / "processed" / "splits" / "rwf2000_split.json"))
    parser.add_argument("--seed",  type=int, default=42)
    parser.add_argument("--train", type=float, default=0.70)
    parser.add_argument("--val",   type=float, default=0.15)
    args = parser.parse_args()

    root = Path(args.root)
    print(f"\n  Collecting clips from {root}...")
    clips_by_label = collect_clips(root)

    for label, clips in clips_by_label.items():
        print(f"  {label}: {len(clips)} clips found")

    split = stratified_split(
        clips_by_label,
        train_ratio=args.train,
        val_ratio=args.val,
        seed=args.seed,
    )

    print_summary(split)

    # Add split metadata.
    output = {
        "meta": {
            "dataset":     "RWF-2000",
            "seed":        args.seed,
            "train_ratio": args.train,
            "val_ratio":   args.val,
            "test_ratio":  round(1.0 - args.train - args.val, 2),
            "label_map":   LABEL_MAP,
        },
        "train": split["train"],
        "val":   split["val"],
        "test":  split["test"],
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as f:
        json.dump(output, f, indent=2)

    print(f"  Saved → {out}")
    print(f"  Use this file for all models M1, M2, M3, M4.\n")
