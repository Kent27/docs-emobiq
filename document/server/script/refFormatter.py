import os
import re
from urllib.parse import urlparse, urlunparse

def find_and_replace_markdown_images(directory):
    # Recursively traverse the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                replace_markdown_images(file_path)

def remove_query_param(url):
    parsed = urlparse(url)
    parsed = parsed._replace(query='')
    return urlunparse(parsed)

def replace_markdown_images(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Find and replace the markdown images
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, content)
    # print(matches)
    for alt_text, match in matches:
        if ".png" in match:
            # print(match)
            png_file = os.path.basename(match)
            png_file = os.path.normpath(png_file)
            png_file = remove_query_param(png_file)
            new_image = f"![](./{png_file})"
            # print(new_image)
            content = content.replace(f"![{alt_text}]({match})", new_image)

    # print(content)
    with open(file_path, "w") as file:
        file.write(content)
        # print("done")

# Example usage
directory = "./server"
find_and_replace_markdown_images(directory)
