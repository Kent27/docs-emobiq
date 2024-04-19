# read

## Description

Read a file and return the data based on the requested dataType.

## Note

This function cannot be tested on preview.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| fileName | name of the file. | Text | - | - | Yes |
| folder | folder path to the selected file. | Text | - | - | - |
| dataType | dataType to return (base64, text, blob). | Text | - | Base64, Text, Byte_Array | Yes |
| extra | extra parameter to pass into callback. | Text | - | - | - |

## Output

Formatted Result

## Callback

### callback

The function to be executed when the file read is successfully executed.

### errorCallback

The function to be executed when the file read is unsuccessfully executed.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

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

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links
