# Download Organizer

A Python automation tool that organizes downloaded files by file type into designated folders.

## Features

- Automatically monitors the Downloads folder
- Organizes files into categories based on file extensions
- Creates organized folder structure (Documents, Images, Videos, Archives, etc.)
- Moves files to appropriate directories
- Handles duplicates and naming conflicts

## Prerequisites

- Python 3.6+
- Operating System: Windows, macOS, or Linux

## Installation

1. Clone or download this project
2. No external dependencies required (uses standard library)

## Usage

```python
python download_organizer.py
```

## File Organization

Files are organized by type:

- **Documents**: .pdf, .docx, .txt, .xlsx, .pptx
- **Images**: .jpg, .jpeg, .png, .gif, .bmp, .svg
- **Videos**: .mp4, .avi, .mkv, .mov, .wmv
- **Audio**: .mp3, .wav, .flac, .aac
- **Archives**: .zip, .rar, .7z, .tar, .gz
- **Programs**: .exe, .msi, .app
- **Other**: All other file types

## Configuration

Modify the file extensions and folder names in the script to customize organization rules.

## License

MIT License
