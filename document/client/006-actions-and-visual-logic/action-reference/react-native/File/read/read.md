# File.read

## Description

Reads an existing file in the cache directory of the mobile phone and returns its content.

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

## Example

The user wants to read the file content (this example will only works after the user has created a file using `File.write` function).

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](./read-step-1.png) | Drag a button component to a page in the mobile designer. |
| 2. | ![](./read-step-2.png) | Select the event `press` and drag the `File.read` function to the event flow and fill in the parameter. |
| 3. | ![](./read-step-3.png) | Open the installed app on a device with a debugger on and try to press the Button, if the file exist user should be able to see the content on the console. |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

Should be able to see the content of a file from user device.