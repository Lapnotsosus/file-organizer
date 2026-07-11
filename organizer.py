from pathlib import Path
import shutil

# Folder to organize
SOURCE_FOLDER = Path.home() / "Downloads"

# Extension -> Folder mapping
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
    "Code": [".py", ".cpp", ".c", ".java", ".js", ".html", ".css", ".json"],
}

def get_category(extension):
    extension = extension.lower()

    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder

    return "Others"

def organize():
    if not SOURCE_FOLDER.exists():
        print("Folder not found.")
        return

    moved = 0

    for item in SOURCE_FOLDER.iterdir():

        if item.is_dir():
            continue

        category = get_category(item.suffix)

        destination = SOURCE_FOLDER / category
        destination.mkdir(exist_ok=True)

        shutil.move(str(item), destination / item.name)
        moved += 1

    print(f"Done! Moved {moved} files.")

if __name__ == "__main__":
    organize()