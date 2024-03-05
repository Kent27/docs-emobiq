# remove

## Description

Remove a file.

## Note

This function cannot be tested on preview.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| fileName | name of the file to be removed. | Text | - | - | Yes |
| folder | folder path to the selected file. | Text | - | - | - |
| extra | extra parameter to pass into callback. | Text | - | - | - |

## Output

Formatted Result

## Callback

### callback

The function to be executed when the file remove is successfully executed.

### errorCallback

The function to be executed when the file remove is unsuccessfully executed.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to remove a file from their device (this example will only works after the user has created a file using `File.write` function).

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](./remove-step-1.png) | Drag a button component to a page in the mobile designer. |
| 2. | ![](./remove-step-2.png) | Select the event `press` and drag the `File.remove` function to the event flow and fill in the parameter. |
| 3. | ![](./remove-step-3.png) | Open the installed app on a device and try to press the Button, the selected file should be deleted |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

Should be able to remove a file from user device.

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links
