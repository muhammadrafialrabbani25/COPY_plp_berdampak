# Proyek Kelompok

Repositori ini milik kelompok Anda. Semua artefak proyek (kode, dokumen, desain, refleksi, dan percakapan dengan AI) disimpan di sini.
Tugas, tutorial, materi, dan petunjuk ada di repositori materi: `plpberdampak2026/course-materials` (ganti `ORG` dengan nama organisasi).

## Struktur folder

- `src/` — kode Python proyek.
- `tests/` — tes untuk kode Anda.
- `docs/` — laporan, desain, dan catatan refleksi.
- `ai-logs/` — **percakapan dengan AI** (wajib, lihat di bawah).

## Persiapan

Butuh Python 3.12 dan Git.

```bash
pip install -e ".[dev]"
pytest
```

Untuk mengurai bahasa tertentu dengan tree-sitter, tambahkan paket grammar-nya di `pyproject.toml` pada bagian `dependencies`.

## Aturan kerja

1. **Setiap perubahan lewat pull request.** Jangan commit langsung ke `main`. Bagi pekerjaan antar anggota, dan saling tinjau pull request.
2. **Unggah semua chat AI ke `ai-logs/`.** Menggunakan AI diperbolehkan sepenuhnya, tetapi percakapannya wajib diunggah.
   - Format berkas `.md` atau `.txt`.
   - Nama berkas `YYYY-MM-DD-topik.md`, misalnya `2026-12-01-parser-awal.md`.
   - Unggah **percakapan lengkap**, bukan potongan pilihan.
3. **Isi checkpoint.** Setiap Senin, Rabu, dan Jumat sampai 20 Januari 2027, sebuah issue `Checkpoint YYYY-MM-DD` dibuka otomatis. Edit isi issue itu dan jawab empat bagiannya:
   1. Yang diperbaiki sejak checkpoint lalu
   2. Tautan pull request
   3. Tautan chat AI baru
   4. Rencana berikutnya

   **Batas pengisian: pukul 23:59 pada hari checkpoint dibuka.**
4. **Perbaikan berulang dan inisiatif dinilai.** Dosen melihat proses Anda memperbaiki pekerjaan dari waktu ke waktu, bukan hanya hasil akhir.

## Konsekuensi

Chat AI yang **tidak diunggah** mengakibatkan **pemotongan nilai**.

## Umpan balik

Dosen memberi komentar di pull request dan di pull request bernama *Feedback*. Baca dan tanggapi komentar itu pada perbaikan berikutnya.
