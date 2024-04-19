import os
import re
import glob

# Global variable
summary_content = []

def process(folder_path):
    # Variables to use
    README = "README.md"

    print(sorted(os.listdir(folder_path)))


def process_folder(folder_path):
   

    # Traverse through the folder
    for root, dirs, files in os.listdir(folder_path):
        # Check if it's a directory (not a file or symlink)
        if os.path.isdir(os.path.join(root, dirs)):
            subfolder_path = os.path.join(root, dirs)
            # Recursively process subfolder
            process_subfolder(subfolder_path)

        # Check for missing README.md assuming there are no .md files
        if len(glob.glob("*.md", root_dir=root)) == 0 and not os.path.exists(os.path.join(root, README)):
            # Get the folder name
            folder_name = os.path.basename(root)
            # Remove numbers and dashes at beginning
            clean_folder_name = re.sub(r"^(\d+-){1,2}", "", folder_name)
            # Replace dashes with spaces and capitalize words
            clean_folder_name = re.sub(r"-", " ", clean_folder_name).title()
            # Write the new README file
            with open(os.path.join(root, README), "w") as f:
                f.write(f"# {clean_folder_name}\n")

        # Generate table of contents entries
        for filename in files:
            if filename.endswith(".md") and filename != README:
                # Remove the extension
                clean_filename, _ = os.path.splitext(filename)
                # Remove numbers and dashes at beginning
                clean_filename = re.sub(r"^\d+-+", "", clean_filename)
                # Replace dashes with spaces and capitalize words
                clean_filename = re.sub(r"-", " ", clean_filename).title()
    
                relative_path = os.path.relpath(os.path.join(root, filename), folder_path)
                # print(depth)
                indent_str = "  " * depth
                summary_content.append(f"{indent_str}* [{clean_filename}]({relative_path})")

    # Create or update SUMMARY.md
    summary_path = os.path.join(folder_path, "SUMMARY.md")
    if summary_content:
        toc_content = "\n".join(summary_content)
        summary_text = f"# Table of contents\n\n{toc_content}"
        print(summary_text)
        with open(summary_path, "w") as f:
            f.write(summary_text)

def process_subfolder(subfolder_path):
  process_folder(subfolder_path) 

# The main entry point of the script
# The purpose of this script is:
# 1. to generate the necessary README markdown
# 2. To generate the summary based on the files
if __name__ == "__main__":
    # Make sure to run where this python is
    current_path = os.getcwd()

    # Client documentation
    client_path = "../document/client"
    process(os.path.join(current_path, client_path))

    # Server documentation
    server_path = "../document/server"
    process(os.path.join(current_path, server_path))

    print("Processing completed, ready for deployment to gitbook.")