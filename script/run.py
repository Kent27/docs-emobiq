import os
import re
import glob

# Global variable
README = "README.md"
SUMMARY = "SUMMARY.md"
summary_content = []

# Exclude the folders in capitalization
# including their children
excludes_capitalization = [
    # Cordova Functions
    "cordova",
    "react-native",
    # React Native Functions
    "005-function"
]

def process(root_path):

    # Validate if it is a valid folder path
    if not os.path.isdir(root_path):
        print(f"Invalid folder path `{root_path}`")
        return False

    # Process the folders with the initial indentation
    process_folder(root_path, root_path, -1, True)

    # Create or update SUMMARY.md
    summary_path = os.path.join(root_path, SUMMARY)
    if summary_content:
        toc_content = "\n".join(summary_content)
        summary_text = f"# Table of contents\n\n{toc_content}"
        with open(summary_path, "w") as f:
            f.write(summary_text)

    return True

def process_folder(root_folder, folder_path, indent, capitalize):

    # Get the folder name
    folder_name = os.path.basename(folder_path)
    # Remove numbers and dashes at beginning
    clean_folder_name = re.sub(r"^(\d+-){1,2}", "", folder_name)
    # Replace dashes with spaces and capitalize words
    clean_folder_name = re.sub(r"-", " ", clean_folder_name).title()

    # README file location
    file_read_me = os.path.join(folder_path, README)

    # Generate the readme only if necessary, exception files with md
    total_files_markdown = len(glob.glob("*.md", root_dir=folder_path))
    if total_files_markdown == 0 and not os.path.exists(file_read_me):
        with open(file_read_me, "w") as f:
            f.write(f"# {clean_folder_name}\n")

    # Generate table of contents for folder,
    # only for folders with README.md
    if os.path.exists(file_read_me):
        relative_path = os.path.relpath(file_read_me, root_folder)
        summary_content.append("  " * indent + f"* [{clean_folder_name}]({relative_path})")
   
    # Sort the folders and files based on name
    items = sorted(os.listdir(folder_path))

    # Manipulate the indentation if there are multiple markdown files
    # to format it correctly
    if total_files_markdown > 1:
        indent += 1

    # Run through through the folder
    for item_name in items:
        # Check if it's a directory (not a file or symlink)
        item = os.path.join(folder_path, item_name)

        # Process the item
        if os.path.isdir(item):
            # Check when to stop capitalizing
            if capitalize and item_name in excludes_capitalization:
                capitalize = False

            # Recursively process subfolder
            process_folder(root_folder, item, indent + 1, capitalize)
        elif os.path.isfile(item) and item_name.endswith(".md") and item_name != README and item_name != SUMMARY:
            # Remove the extension
            clean_filename, _ = os.path.splitext(item_name)
            # Remove numbers and dashes at beginning
            clean_filename = re.sub(r"^\d+-+", "", clean_filename)
            # Replace dashes with spaces
            clean_filename = re.sub(r"-", " ", clean_filename)

            # Capitalize words if necessary
            if capitalize:
                clean_filename = clean_filename.title()

            # Generate table of contents entries
            relative_path = os.path.relpath(item, root_folder)
            summary_content.append("  " * indent + f"* [{clean_filename}]({relative_path})")

# The main entry point of the script
# The purpose of this script is:
# 1. to generate the necessary README markdown
# 2. To generate the summary based on the files
if __name__ == "__main__":

    # Make sure to run where this python is
    current_path = os.getcwd()

    # Client documentation
    client_path = "../document/client"
    summary_content = []
    if not process(os.path.join(current_path, client_path)):
        exit()

    # Server documentation
    server_path = "../document/server"
    summary_content = []
    if not process(os.path.join(current_path, server_path)):
        exit()

    print("Processing completed, ready for deployment to gitbook.")