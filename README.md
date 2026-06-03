# Violence Detection Research

Repository nghiên cứu phát hiện bạo lực trong video, tập trung vào pipeline:

1. Kiểm tra và chuẩn hóa dataset RWF-2000/RLVS.
2. Fine-tune base detector X3D-S trên RWF-2000.
3. Trích xuất context features: crowd, lighting, motion.
4. Train Context Gating Module (CGM) và chạy ablation để đo FPR/FNR.
5. So sánh thêm các detector hiện đại như SwinV2, ConvNeXt, EfficientNetV2.

## Project Structure

```text
.
├── src/violence_detection/      # Code tái sử dụng: dataset, model/utils sau này
├── scripts/                     # Các phase chạy experiment
├── data/
│   ├── raw/                     # Dataset thật, không commit lên Git
│   └── processed/splits/        # Split JSON có thể commit để reproducible
├── docs/
│   ├── research/                # Paper, literature matrix, research questions
│   ├── datasets/                # Dataset protocol và checklist
│   ├── project_plan/            # Timeline 4 tuần
│   └── evidence/                # Decision log và AI audit log
├── outputs/                     # Checkpoint/cache/result nặng, không commit
├── reports/                     # Báo cáo nhỏ có thể dùng làm evidence
└── configs/                     # Cấu hình experiment nếu cần mở rộng
```

## Environment Setup

Yêu cầu khuyến nghị:

- Python 3.10
- PyTorch 2.x
- CUDA phù hợp với GPU đang dùng
- PyTorchVideo, Ultralytics, OpenCV, scikit-learn, pandas, wandb
- Git + Git LFS nếu lưu metadata lớn hoặc artifact đặc biệt

Tạo môi trường:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

Kiểm tra nhanh:

```powershell
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

## Dataset Layout

Không commit dataset video vào Git. Đặt dữ liệu như sau:

```text
data/raw/RWF-2000/
├── train/fight/
├── train/nonFight/
├── val/fight/
└── val/nonFight/

data/raw/RLVS/
```

Split chính đang ở:

```text
data/processed/splits/rwf2000_split.json
```

## Reproducible Workflow

Chạy theo thứ tự:

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

Các file nên cập nhật trước khi push/nộp:

- `docs/research/related_work.pdf`: nội dung related work/literature review đã soạn.
- `docs/project_plan/timeline_and_research_questions.pdf`: bản tổng hợp timeline và research questions.
- `docs/research/literature_review_matrix.md`: tóm tắt tối thiểu 5 paper.
- `docs/research/research_questions.md`: RQ, metric, hypothesis, evidence.
- `docs/datasets/dataset_protocol.md`: nguồn dataset, kiểm tra integrity, mapping label.
- `docs/project_plan/timeline_4_weeks.md`: timeline và deliverable từng tuần.
- `docs/evidence/ai_audit_log.md`: prompt/decision log khi dùng AI hỗ trợ.
- `reports/dataset/`: thống kê và lỗi dataset sau khi chạy phase 0.
