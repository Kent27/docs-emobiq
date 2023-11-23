# File.read

## Description

Reads an existing file in the server and returns its content.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| fileName | The name of the file to read. | Text | - | - | Yes |
| folder | The folder path of the file. If this input is provided, it will be appended to the storage path. | Text | - | - | No |
| dataType | The type of data to return. | Text | - | Base64, Text, Byte_Array | Yes |
| extra | The stored value that is passed to all the callbacks. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| success | Boolean value to denote whether the function was executed successfully. | Text |
| message | The message to print. | Text |
| data | Any additional message or data to print. | Text |

## Callback

### callback

The action performed if this function runs successfully.

| Description | Output Type |
| ------ | ------ |
| Returns the file content based on the user's choice of data type. | Any |

### errorCallback

The action performed if this function does not run successfully.

| Description | Output Type |
| ------ | ------ |
| Returns an error message. | Text |

## Video

Coming Soon.

## Example

Coming Soon.

### Steps

Coming Soon.

### Result

Coming Soon.

## Links