# File.write

## Description

Creates a new file or overrides an existing file in the server.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| data | The file data to write. | Text | - | Base64, Text, Byte array | Yes |
| dataType | The type of file content. | Text | - | Base64, Text, Byte array | Yes |
| fileName | The name of the file to write. | Text | - | - | Yes |
| folder | The folder path of the file. If this input is provided, it will be appended to the storage path. | Text | - | - | No |
| extra | The stored value that is passed to all the callbacks. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| success | Boolean value to denote whether the fucntion was executed successfully. | Text |
| message | The message to print. | Text |
| data | Any additional message or data to print. | Text |

## Callback

### callback

The action performed if this function runs successfully.

| Description | Output Type |
| ------ | ------ |
| Returns an object that contains the file information. | Object |

### errorCallback

The action performed if this function does not run successfully.

| Description | Output Type |
| ------ | ------ |
| Returns an error message. | Text |

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

Coming Soon.

<!-- Share a scenario, like a user requirements. -->

### Steps

Coming Soon.

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}?raw=true) -->

### Result

Coming Soon.

<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links