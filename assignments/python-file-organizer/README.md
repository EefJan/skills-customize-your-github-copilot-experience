# 📘 Assignment: Python File Organizer

## 🎯 Objective

Create a helpful Python script that organizes files in a folder by type, making it easier to manage cluttered directories and practice working with Python file operations.

## 📝 Tasks

### 🛠️ Build the Organizer Script

#### Description
Write a script that scans a folder and moves files into new subfolders based on their file extension.

#### Requirements
Completed program should:

- Accept a target folder path as input.
- Look through the files in that folder.
- Group files by extension such as `.txt`, `.jpg`, `.pdf`, or `.py`.
- Create a folder for each file type if it does not already exist.
- Move each file into the matching folder.
- Print a message showing how many files were organized.

### 🛠️ Handle Common Edge Cases

#### Description
Improve the script so it behaves safely when working with real folders.

#### Requirements
Completed program should:

- Ignore folders and only process files.
- Skip files already in the correct destination folder.
- Avoid crashing if a folder does not exist.
- Display a clear summary after the script runs.

### 🛠️ Make It User-Friendly

#### Description
Add a few small features that make the organizer easier to use and understand.

#### Requirements
Completed program should:

- Use `pathlib` or `os` to work with files and directories.
- Include a clear function or functions for organizing files.
- Provide a simple way to run the script from the terminal.
- Example command:

```bash
python organizer.py my_folder
```
