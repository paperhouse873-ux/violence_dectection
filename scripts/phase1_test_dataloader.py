"""
Phase 1 — Test RWF-2000 Dataset/DataLoader.

Run:
  python scripts/phase1_test_dataloader.py ^
    --root data/raw/RWF-2000 ^
    --split data/processed/splits/rwf2000_split.json
"""

import argparse

from _bootstrap import PROJECT_ROOT
from violence_detection.datasets.rwf2000 import test_dataloader


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=str,
        default=str(PROJECT_ROOT / "data" / "raw" / "RWF-2000"),
        help="Path to the RWF-2000 dataset root",
    )
    parser.add_argument(
        "--split",
        type=str,
        default=str(PROJECT_ROOT / "data" / "processed" / "splits" / "rwf2000_split.json"),
        help="Path to the reproducible split JSON",
    )
    args = parser.parse_args()

    test_dataloader(args.root, args.split)
