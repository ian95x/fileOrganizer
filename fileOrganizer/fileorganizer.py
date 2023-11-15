import os
import shutil

def organize_files(source_dir, dest_dir):
    # Create a dictionary to map file extensions to their respective folders
    extension_to_folder = {
        ".pdf": "PDFs",
        ".docx": "Documents",
        ".xlsx": "Spreadsheets",
        ".jpg": "Images",
        ".png": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".mp3": "Audio",
    }

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over the files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Check if the file is a regular file
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]

            # Determine the destination folder for the file
            if file_extension in extension_to_folder:
                destination_folder = os.path.join(dest_dir, extension_to_folder[file_extension])
            else:
                destination_folder = dest_dir

            # Move the file to the destination folder
            shutil.move(file_path, destination_folder)

if __name__ == "__main__":
    # Get the source directory from the user
    source_dir = input("Enter the source directory: ")

    # Get the destination directory from the user
    dest_dir = input("Enter the destination directory: ")

    # Organize the files
    organize_files(source_dir, dest_dir)

