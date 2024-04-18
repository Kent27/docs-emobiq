# canvasResize

## Description

Resize an existing canvas, canvas are mainly used for printing.

## Input / Parameter

| Name | Description | Data Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| canvas | An existing canvas to be copied over to the new canvas. |[HTMLCanvasElement](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas) | - | - | Yes |
| canvasWidth | Width of the new resized canvas. | Number | - | - | No | 
| canvasHeight | Height of the new resized canvas. | Number | - | - | No | 
| extra | Additional data to be used in the callbacks. | Any | - | - | No | 

## Output

| Description | Output Type |
| ------ | ------ |
| Returns 'true' or 'false', if it was executed successfully. | Boolean |

## Callback

### callback

The function to be executed when the canvas is resized successfully.

| Description | Output Type |
| ------ | ------ |
| Returns the html canvas. | [HTMLCanvasElement](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas) |

### errorCallback

The function to be executed when the canvas is not resized successfully.

| Description | Output Type |
| ------ | ------ |
| Returns the error. | Text |