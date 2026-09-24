from pathlib import Path


def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print(f"Folder not found: {folder}")
        return

    # TODO: loop through files in the folder
    # TODO: create a subfolder for each file extension
    # TODO: move files into the matching folder
    # TODO: print a summary of organized files

    print(f"Organization complete for: {folder}")


if __name__ == "__main__":
    target = input("Enter the folder path to organize: ")
    organize_files(target)
