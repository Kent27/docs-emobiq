import os
import subprocess

# Read the SUMMARY.md file
with open("SUMMARY.md", "r", encoding="utf-8") as summary_file:
    lines = summary_file.readlines()

# Create a temporary combined Markdown file
with open("combined.md", "w", encoding="utf-8") as combined_file:
    for line in lines:
        if line.strip().startswith("* ["):
            # Extract the file path from the line
            file_path = line.split("](")[1].split(")")[0]
            # Check if the file exists
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as markdown_file:
                    combined_file.write(markdown_file.read())
            else:
                print(f"File not found: {file_path}")

# # Use Pandoc to convert the combined Markdown to PDF
# subprocess.run(["pandoc", "combined.md", "-o", "output.pdf"])

# # Clean up the temporary combined Markdown file
# os.remove("combined.md")
