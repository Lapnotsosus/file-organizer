# 📂 File Organizer

A lightweight Python utility that automatically organizes files into folders based on their file extensions.

## Features

* Automatically categorizes files by type
* Creates folders if they don't already exist
* Supports:

  * 🖼️ Images
  * 🎥 Videos
  * 🎵 Music
  * 📄 Documents
  * 📦 Archives
  * 💻 Source Code
  * ⚙️ Programs
  * 📁 Others
* Easy to customize by editing the extension mapping
* Uses only Python's standard library (no external dependencies)

## Project Structure

```text
file-organizer/
├── organizer.py
└── README.md
```

## How It Works

The script:

1. Scans the target folder.
2. Determines each file's type using its extension.
3. Creates a destination folder if necessary.
4. Moves the file into the appropriate category.

For example:

### Before

```text
Downloads/
├── photo.png
├── report.pdf
├── music.mp3
├── project.py
├── archive.zip
```

### After

```text
Downloads/
├── Images/
│   └── photo.png
├── Documents/
│   └── report.pdf
├── Music/
│   └── music.mp3
├── Code/
│   └── project.py
├── Archives/
│   └── archive.zip
```

## Installation

Clone the repository:

```bash
git clone https://github.com/lapnotsosun/file-organizer.git
```

Move into the project folder:

```bash
cd file-organizer
```

## Usage

Edit the `SOURCE_FOLDER` variable in `organizer.py` if you want to organize a different directory.

Run the script:

```bash
python organizer.py
```

## Built With

* Python 3
* `pathlib`
* `shutil`

## Future Improvements

* GUI using Tkinter
* Drag-and-drop folder selection
* Undo last operation
* Organize by creation date
* Duplicate file detection
* Real-time folder monitoring
* Configuration file support

## License

This project is open source and available under the MIT License.
