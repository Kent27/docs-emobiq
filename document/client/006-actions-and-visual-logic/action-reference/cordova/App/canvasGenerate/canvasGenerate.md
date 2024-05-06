# canvasGenerate

## Description

Generate base64 from an existing canvas, 

### Platform Supported

- Web
- Mobile

## Input / Parameter

| Name | Description | Data Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| canvas | An existing canvas to be copied over to the new canvas. | Text | - | - | Yes |
| canvasWidth | Width of the new canvas. | Number | 300 | - | No | 
| canvasHeight | Height of the new canvas. | Number | 300 | - | No | 
| extra | Additional data to be used in the callbacks. | Any | - | - | No | 

## Output

N/A

## Callback

### callback

The function to be executed when converting the canvas to base64 was successful.

| Description | Output Type |
| ------ | ------ |
| Returns the base64 of the canvas. | Text |

### errCallback

The function to be executed when converting the canvas to base64 was not successful.

| Description | Output Type |
| ------ | ------ |
| Returns the error. | Text |