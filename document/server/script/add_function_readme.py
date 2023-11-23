import os

def create_readme(path):
    folder_name = os.path.basename(path)
    readme_path = os.path.join(path, "README.md")
    
    # Check if README.md already exists
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as file:
            file.write(f"# {folder_name}\n")
            print(folder_name)

def main(directory):
    # Iterate through all directories within the specified directory
    for foldername, subfolders, filenames in os.walk(directory):
        create_readme(foldername)

if __name__ == "__main__":
    directory = "./server/server/function"
    main(directory)
    print(f"README.md files have been added to all folders within {directory}!")
