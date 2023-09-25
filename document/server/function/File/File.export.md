# File.export

## Description

Exports and downloads data as Excel or CSV file.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| data | The list of objects to be exported. Multiple dynamic attributes with values associated with each attribute. | List | - | - | Yes |
| fileName | The name of the file that will be downloaded. | Text | - | - | Yes |
| fileType | The type of file to create. | Text | Excel | Excel, CSV | Yes |
| sheetName | The worksheet within the file to write data to. By default, the worksheet name will be 'Sheet 1'. | Text | - | - | No |
| header | To denote whether the data has a header row. | Boolean | - | - | No |
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