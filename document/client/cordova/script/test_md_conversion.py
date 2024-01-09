# import re

# def convert_table(markdown_table):
#     lines = markdown_table.strip().split('\n')
#     headers = [header.strip() for header in lines[0].split('|')[1:-1]]
#     headers = [re.sub(r'\s+', ' ', header) for header in headers]

#     rows = [re.sub(r'\s+', ' ', row).split('|')[1:-1] for row in lines[2:]]
#     formatted_rows = []

#     for row in rows:
#         formatted_row = {headers[i]: cell.strip() for i, cell in enumerate(row)}
#         formatted_rows.append(formatted_row)

#     output = ""
#     for row in formatted_rows:
#         output += f"**{row['Name']}**\n"
#         for header in headers[1:]:
#             output += f"  - {header}: {row[header]}\n"
#         output += "\n"

#     return output

# markdown_table = """
# | Name | Description | Data Type | Default | Options | Required |
# | ------ | ------ | ------ | ------ | ------ | ------ |
# | text | The text with a specific format to be drawn in the canvas. See text format after this table. | String/Text | - | - | No |
# | font | The name of the font to be used. | String/Text | monospace | monospace, ocrb | No | 
# | size | The size of the font to be used with the suffix 'px' for pixel. | String/Text | 23px | - | No | 
# | canvasWidth | The width of the canvas. | Number | 576 | - | No | 
# | marginTop | The margin top value of the canvas. | Number | 0 | - | No | 
# | marginLeft | The margin left value of the canvas. | Number | 0 | - | No | 
# | marginRight | The margin right value of the canvas. | Number | 0 | - | No | 
# | marginBottom | The margin bottom value of the canvas. | Number | 0 | - | No | 
# """

# converted_output = convert_table(markdown_table)
# print(converted_output)

import re
import os

def convert_table(markdown_table):
    lines = markdown_table.strip().split('\n')
    headers = [header.strip() for header in lines[0].split('|')[1:-1]]
    headers = [re.sub(r'\s+', ' ', header) for header in headers]

    rows = [re.sub(r'\s+', ' ', row).split('|')[1:-1] for row in lines[2:]]
    formatted_rows = []
    # Append for missing rows
    # num_to_append = len(headers) - len(rows)
    # for i in range(num_to_append):
    #     rows.extend('-')
    for row in rows:
        # formatted_row = {headers[i]: cell.strip() for i, cell in enumerate(row)}
        # formatted_rows.append(formatted_row)
        formatted_row = {}
        for i, cell in enumerate(row):
            formatted_row[headers[i]] = cell.strip()
        formatted_rows.append(formatted_row)

    output = ""
    for row in formatted_rows:
        if 'Name' in row:
            # print(headers)
            # print(rows)
            output += f"**{row['Name']}**\n"
            for header in headers[1:]:
                output += f"  - {header}: {row[header]}\n"
            output += "\n"
        else:
            # print(headers)
            for header in headers:
                output += f"  - {header}: {row[header]}\n"
            output += "\n"

    return output

def convert_markdown_with_tables(input_markdown):
    lines = input_markdown.split('\n')
    output = []
    table_buffer = []

    inside_table = False
    for line in lines:
        if line.strip().startswith('|') and inside_table:
            table_buffer.append(line)
        elif line.strip().startswith('|') and not inside_table:
            inside_table = True
            table_buffer.append(line)
        elif not line.strip().startswith('|') and inside_table:
            inside_table = False
            output.append(convert_table('\n'.join(table_buffer)))
            table_buffer = []
            output.append(line)
        else:
            output.append(line)

    if table_buffer:
        output.append(convert_table('\n'.join(table_buffer)))

    return '\n'.join(output)

def find_and_replace_markdown_tables(directory):
    # Recursively traverse the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as file:
                    content = file.read()
                print(file_path)
                contents = convert_markdown_with_tables(content)
                with open(file_path, "w") as file:
                    file.write(contents)
                    print('Done', file_path)

directory = "./document"
converted_output = find_and_replace_markdown_tables(directory)

#TEST
# input_markdown = """
# # canvasToDataURL?

# ## Description

# Convert the value in a signature component to dataURL eg data:__[__&lt;mediatype&gt;__]__[_;base64_]_,&lt;data&gt; 

# ## Input / Parameter

# | No | Name | Description | Data Type | Required | Example |
# | ------ | ------ | ------ |------ | ------ | ------ |
# | 1 | canvas | The name of signature component. | String/Text | Yes | |

# ## Output

# | Description | Output Type |
# | ------ | ------ |
# | Returns true if the canvas was converted, returns false otherwise. | Boolean |

# ## Callback

# N/A

# ## Video

# Coming Soon.

# <!-- Format: [![Video]({image-path})]({url-link}) -->

# ## Example

# Coming Soon.

# <!-- Share a scenario, like a user requirements. -->

# ### Steps

# Coming Soon.

# <!-- Show the steps and share some screenshots.

# 1. .....

# Format: ![]({image-path}) -->

# ### Result

# Coming Soon.

# <!-- Explain the output.

# Format: ![]({image-path}) -->

# ## Links
# """
# print(convert_markdown_with_tables(input_markdown))
# print(converted_output)

# with open('./output_test.md', "w") as f:
#     f.write(converted_output)