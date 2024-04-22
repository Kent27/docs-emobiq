import os
import re
import glob

# Global variable
README = "README.md"
summary_content = []

def process(folder_path):

    # Validate if it is a valid folder path
    if not os.path.isdir(folder_path):
        print(f"Invalid folder path `{folder_path}`")
        return False

    # Process the folders with the initial indentation
    process_folder(folder_path, 0)

    # Create or update SUMMARY.md
    summary_path = os.path.join(folder_path, "SUMMARY.md")
    if summary_content:
        toc_content = "\n".join(summary_content)
        summary_text = f"# Table of contents\n\n{toc_content}"
        with open(summary_path, "w") as f:
            f.write(summary_text)

    return True

def process_folder(folder_path, indent):

    # Check for missing README.md assuming there are no .md files
    # generate a readme file for gitbook proper format
    if len(glob.glob("*.md", root_dir=folder_path)) == 0 and not os.path.exists(os.path.join(folder_path, README)):
        # Get the folder name
        folder_name = os.path.basename(folder_path)
        # Remove numbers and dashes at beginning
        clean_folder_name = re.sub(r"^(\d+-){1,2}", "", folder_name)
        # Replace dashes with spaces and capitalize words
        clean_folder_name = re.sub(r"-", " ", clean_folder_name).title()
        # Write the new README file
        with open(os.path.join(folder_path, README), "w") as f:
            f.write(f"# {clean_folder_name}\n")
   
    # Sort the folders and files based on name
    items = sorted(os.listdir(folder_path))

    # Run through through the folder
    for item_name in items:
        # Check if it's a directory (not a file or symlink)
        item = os.path.join(folder_path, item_name)

        # Process the item
        if os.path.isdir(item):
            # Recursively process subfolder
            process_folder(item, indent + 1)
        elif os.path.isfile(item) and item.endswith(".md") and item != README:
            # Remove the extension
            clean_filename, _ = os.path.splitext(item)
            # Remove numbers and dashes at beginning
            clean_filename = re.sub(r"^\d+-+", "", clean_filename)
            # Replace dashes with spaces and capitalize words
            clean_filename = re.sub(r"-", " ", clean_filename).title()

            # Generate table of contents entries
            relative_path = os.path.relpath(os.path.join(folder_path, item), folder_path)
            summary_content.append(f"{"  " * indent}* [{clean_filename}]({relative_path})")

# The main entry point of the script
# The purpose of this script is:
# 1. to generate the necessary README markdown
# 2. To generate the summary based on the files
if __name__ == "__main__":
    # Make sure to run where this python is
    current_path = os.getcwd()

    # Client documentation
    client_path = "../document/client"
    if not process(os.path.join(current_path, client_path)):
        exit()

    # Server documentation
    server_path = "../document/server"
    if not process(os.path.join(current_path, server_path)):
        exit()

    print("Processing completed, ready for deployment to gitbook.")