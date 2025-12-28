# Snapshot Backup CLI

Snapshot Backup CLI adalah tools backup **offline** berbasis command-line
untuk melakukan snapshot file dan folder secara cepat dan aman.
Dikemas menjadi **satu file .exe**, tanpa cloud, tanpa instalasi tambahan.

## Fitur Utama
- Snapshot file
- Snapshot folder
- Restore snapshot
- Logging aktivitas backup & restore
- Portable (cukup 1 file .exe)

## Cara Menggunakan
1. Jalankan `snapshot_backup.exe`
2. Pilih menu:
   - Snapshot File
   - Snapshot Folder
   - Restore Snapshot
3. Folder `backup/` akan dibuat otomatis di lokasi tool dijalankan

## Struktur Folder
backup/
├── snapshots/
│ ├── 2025-01-01_10-00-00/
│ └── 2025-01-01_11-00-00/
└── backup.log

## Catatan Penting
- Tools ini **100% offline**
- Tidak mengirim data ke internet
- Simpan file `.exe` di satu folder khusus
- Disarankan menjalankan tool dengan izin yang cukup (read/write)

## Target Pengguna
- Pengguna umum
- Pelajar
- Pengguna laptop dengan file penting
- Orang yang ingin backup sederhana tanpa cloud

## Status Project
Versi stabil **v1.0.0**  
Project ini adalah **produk kecil offline**, bukan sekadar latihan.

---

Dibangun oleh: Delta
