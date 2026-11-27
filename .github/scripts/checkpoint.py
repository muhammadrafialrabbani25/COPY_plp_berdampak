"""Menentukan judul dan isi issue checkpoint (Senin, Rabu, Jumat sampai 2027-01-20)."""

import argparse
from datetime import date, datetime
from zoneinfo import ZoneInfo

END_DATE = date(2027, 1, 20)
REVIEW_WEEKDAYS = (0, 2, 4)  # Senin, Rabu, Jumat

CHECKPOINT_BODY = """\
Edit isi issue ini dan jawab keempat bagian di bawah.
**Batas pengisian: pukul 23:59 hari ini.**

## 1. Yang diperbaiki
_isi di sini_

## 2. Tautan PR
_isi di sini_

## 3. Tautan chat AI baru
_isi di sini_

## 4. Rencana berikutnya
_isi di sini_
"""


def checkpoint_title(today: date) -> str | None:
    if today > END_DATE or today.weekday() not in REVIEW_WEEKDAYS:
        return None
    return f"Checkpoint {today:%Y-%m-%d}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--today", help="YYYY-MM-DD; default: hari ini di Asia/Jakarta")
    args = parser.parse_args()
    if args.today:
        today = date.fromisoformat(args.today)
    else:
        today = datetime.now(ZoneInfo("Asia/Jakarta")).date()
    title = checkpoint_title(today)
    if title:
        print(title)


if __name__ == "__main__":
    main()
