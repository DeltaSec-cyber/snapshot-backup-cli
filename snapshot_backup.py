import os
import sys
import shutil
from datetime import datetime

# =========================
# BASE PATH (PY + EXE SAFE)
# =========================
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BACKUP_ROOT = os.path.join(BASE_DIR, "backup", "snapshots")
LOG_FILE = os.path.join(BASE_DIR, "backup", "backup.log")

# =========================
# HELPER FUNCTIONS
# =========================
def ensure_dirs():
    os.makedirs(BACKUP_ROOT, exist_ok=True)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


def write_log(message):
    ensure_dirs()
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(message + "\n")


def create_snapshot_folder():
    ensure_dirs()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    snapshot_path = os.path.join(BACKUP_ROOT, timestamp)
    os.makedirs(snapshot_path, exist_ok=True)
    return snapshot_path


def list_snapshots():
    if not os.path.exists(BACKUP_ROOT):
        return []
    return sorted(os.listdir(BACKUP_ROOT))


def ask_path(prompt):
    path = input(prompt).strip()
    if not path:
        print("❌ Input tidak boleh kosong.")
        return None
    return path


def confirm_action(message):
    answer = input(f"{message} (y/n): ").strip().lower()
    return answer == "y"


# =========================
# CORE FEATURES
# =========================
def snapshot_file():
    src = ask_path("Path file sumber: ")
    if not src or not os.path.isfile(src):
        print("❌ File sumber tidak valid.")
        return

    snapshot_path = create_snapshot_folder()
    filename = os.path.basename(src)
    dst = os.path.join(snapshot_path, filename)

    shutil.copy2(src, dst)
    write_log(f"[{datetime.now()}] FILE SNAPSHOT | {src} -> {dst}")
    print("✔ File berhasil di-backup ke snapshot.")


def snapshot_folder():
    src = ask_path("Path folder sumber: ")
    if not src or not os.path.isdir(src):
        print("❌ Folder sumber tidak valid.")
        return

    snapshot_path = create_snapshot_folder()
    folder_name = os.path.basename(src.rstrip("\\/"))
    dst = os.path.join(snapshot_path, folder_name)

    shutil.copytree(src, dst)
    write_log(f"[{datetime.now()}] FOLDER SNAPSHOT | {src} -> {dst}")
    print("✔ Folder berhasil di-backup ke snapshot.")


def restore_snapshot():
    snapshots = list_snapshots()
    if not snapshots:
        print("❌ Tidak ada snapshot untuk direstore.")
        return

    print("\nDaftar Snapshot:")
    for i, name in enumerate(snapshots, start=1):
        print(f"{i}. {name}")

    try:
        choice = int(input("Pilih snapshot: ")) - 1
        snapshot_name = snapshots[choice]
    except (ValueError, IndexError):
        print("❌ Pilihan tidak valid.")
        return

    snapshot_path = os.path.join(BACKUP_ROOT, snapshot_name)
    target_path = ask_path("Path tujuan restore (folder baru): ")
    if not target_path:
        return

    if os.path.exists(target_path):
        print("❌ Folder tujuan sudah ada. Pilih folder baru.")
        return

    if not confirm_action("Lanjutkan restore snapshot ini"):
        print("Restore dibatalkan.")
        return

    try:
        shutil.copytree(snapshot_path, target_path)
        write_log(f"[{datetime.now()}] RESTORE | {snapshot_path} -> {target_path}")
        print("✔ Snapshot berhasil direstore.")
    except Exception as e:
        print("❌ Gagal restore snapshot.")
        write_log(f"[{datetime.now()}] RESTORE ERROR | {e}")


# =========================
# MAIN
# =========================
def main():
    while True:
        print("\n=== SNAPSHOT BACKUP CLI ===")
        print("1. Snapshot File")
        print("2. Snapshot Folder")
        print("3. Restore Snapshot")
        print("4. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            snapshot_file()
        elif pilihan == "2":
            snapshot_folder()
        elif pilihan == "3":
            restore_snapshot()
        elif pilihan == "4":
            print("Keluar dari program...")
            break
        else:
            print("❌ Pilihan tidak valid.")


if __name__ == "__main__":
    main()
