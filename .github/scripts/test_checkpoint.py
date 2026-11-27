from datetime import date

import checkpoint


def test_title_on_review_days():
    assert checkpoint.checkpoint_title(date(2026, 11, 23)) == "Checkpoint 2026-11-23"  # Senin
    assert checkpoint.checkpoint_title(date(2026, 11, 25)) == "Checkpoint 2026-11-25"  # Rabu
    assert checkpoint.checkpoint_title(date(2026, 11, 27)) == "Checkpoint 2026-11-27"  # Jumat


def test_none_on_other_weekdays():
    assert checkpoint.checkpoint_title(date(2026, 11, 24)) is None  # Selasa
    assert checkpoint.checkpoint_title(date(2026, 11, 28)) is None  # Sabtu
    assert checkpoint.checkpoint_title(date(2026, 11, 29)) is None  # Minggu


def test_last_checkpoint_is_2027_01_20():
    assert checkpoint.END_DATE == date(2027, 1, 20)
    assert checkpoint.checkpoint_title(date(2027, 1, 20)) == "Checkpoint 2027-01-20"  # Rabu
    assert checkpoint.checkpoint_title(date(2027, 1, 22)) is None  # Jumat, lewat batas


def test_body_has_four_sections_with_placeholders():
    body = checkpoint.CHECKPOINT_BODY
    for heading in (
        "## 1. Yang diperbaiki",
        "## 2. Tautan PR",
        "## 3. Tautan chat AI baru",
        "## 4. Rencana berikutnya",
    ):
        assert heading in body
    assert body.count("_isi di sini_") == 4
    assert "23:59" in body
