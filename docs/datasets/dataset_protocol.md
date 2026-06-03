# Dataset Protocol

## Datasets

| Dataset | Target Role | Expected Size | Local Folder | Git Policy |
| --- | --- | --- | --- | --- |
| RWF-2000 | Main train/validation/test benchmark | 2,000 clips, balanced violent/non-violent | `data/raw/RWF-2000/` | Do not commit videos |
| RLVS | Secondary validation or transfer dataset | Verify after download | `data/raw/RLVS/` | Do not commit videos |

## RWF-2000 Checklist

1. Download/extract into `data/raw/RWF-2000/`.
2. Verify folder structure:

   ```powershell
   python scripts/phase0_check_structure.py
   ```

3. Verify video integrity:

   ```powershell
   python scripts/phase0_check_integrity.py
   ```

4. Generate statistics:

   ```powershell
   python scripts/phase0_statistics.py
   ```

5. Generate reproducible split:

   ```powershell
   python scripts/phase0_create_split.py
   ```

## Evidence To Keep

- `data/processed/splits/rwf2000_split.json`
- `reports/dataset/dataset_stats.csv`
- `reports/dataset/corrupted_files.txt` if any corrupted clips exist
- Notes about source URL, download date, and license/usage constraints

## Label Mapping

| Folder | Label | Meaning |
| --- | --- | --- |
| `fight` | 1 | violent |
| `nonFight` | 0 | non-violent |
