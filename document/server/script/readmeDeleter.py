import os

def delete_readme_files(directory, level = 0): # Specify which depth onwards to remove readme files
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            delete_readme_files(filepath, level + 1)  # Recursively process subdirectories
        elif filename == 'README.md' and level >=2:
            os.remove(filepath)
            print(f"Deleted {filepath}")

# Example usage
directory_path = './server/function'

# Protects the Readme in the very first directory
delete_readme_files(directory_path)
