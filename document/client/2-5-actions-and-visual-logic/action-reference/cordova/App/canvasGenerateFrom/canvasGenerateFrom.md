# canvasGenerateFrom

## Description

Converts a file data to a canvas, canvas are mainly used for printing.

### Platform Supported

- Web
- Mobile

## Input / Parameter

| Name | Description | Data Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| type | The data type of the file to be converted, basically what is the data type of the 'value'. | Text | base64 | base64 | No |
| value | The data of the file to be converted. | Any | - | - | Yes | 
| fileType | The file type of the file to be converted, basically what is the file type of the 'value'. | Text | image | image, pdf | No | 
| documentSize | If the 'fileType' is 'pdf', this parameter is used to scale the size appropriately. | Text or Number | - | a4, {Any  Number} | No | 

## Output

| Description | Output Type |
| ------ | ------ |
| Returns 'true' or 'false', based on the execution status. | Boolean |

## Callback

### callback

The function to be executed when the canvas is generated successfully.

| Description | Output Type |
| ------ | ------ |
| Returns the html canvas. | [HTMLCanvasElement](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas) |

### errCallback

The function to be executed when the canvas is not generated.

| Description | Output Type |
| ------ | ------ |
| Returns the error. | Text/Object |