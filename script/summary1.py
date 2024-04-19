import os

#todo: Improve the logic. Number of times to minus indent level = number of directories entered without readme. Logic is very wrong now.

# Provide the root directory path and output file path
root_name = 'document'
root_directory = f"./{root_name}"
output_file = "SUMMARY.md"

def generate_summary(directory, level=0, ignoreReadMe=False, parentName=root_name, level_offset=0):
    summary = ""
    indent = "  " * (level-level_offset)

    # Check for any readme in current folder first. Directory name will be printed if readme is present.
    if 'README.md' in os.listdir(directory) and ignoreReadMe == False:
        item_path = os.path.join(directory, 'README.md')
        with open(item_path, "r") as file:
            for line in file:
                if line.startswith("#"):
                    title = line[2:].strip()  # Remove the "# " and any leading/trailing whitespace
                    # print("Title:", title)
                    break  # Exit the loop once the title is found
            else:
                title = parentName
                print(item_path)
                print("No title found.")
        summary += f"{indent}* [{title}]({item_path})\n"
        level += 1

    for item in sorted(os.listdir(directory)):
        currentName = item
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path): # if item is a folder
            # if item == "function": # Ignore all README from children of function
            #     summary += generate_summary(item_path, level + 1, False, currentName)
            # else:
            # if(not "README.md" in os.listdir(directory)):
            #     level_offset += 1
            #     print("added")
            summary += generate_summary(item_path, level, False, currentName, level_offset)
            # if not ignoreReadMe:
            #     summary += f"{indent}* [{item}]({item}/README.md)\n"
            #     summary += generate_summary(item_path, level + 1)
            # else:
            #     summary += generate_summary(item_path, level + 1, True)
        elif item.endswith(".md") and not item.endswith("README.md"):
            if ignoreReadMe == True and item.endswith("README.md"):
                continue
            with open(item_path, "r") as file:
                for line in file:
                    if line.startswith("# "):
                        title = line[2:].strip()  # Remove the "# " and any leading/trailing whitespace
                        # print("Title:", title)
                        break  # Exit the loop once the title is found
                else:
                    title = parentName
                    print(item_path)
                    print("No title found.")
            indent = "  " * (level-level_offset) # To account for the folder that did not print
            # summary += f"{indent}  * [{parentName}]({item_path})\n"
            summary += f"{indent}* [{title}]({item_path})\n"

    return summary

def generate_directory_summary(root_directory, output_file):
    with open(output_file, "w") as f:
        f.write("# Table of contents\n\n")
        f.write(generate_summary(root_directory))

generate_directory_summary(root_directory, output_file)
