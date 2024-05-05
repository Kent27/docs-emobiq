# canvasToDataURL

## Description

Converts a component to base64.

Note: Not all components are supported, as of now only the following are supported:

- Signature
- Barcode
- QRCode

### Platform Supported

- Web
- Mobile

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| canvas | The name of the component. | Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the component. | Text | - | - | Partial (Yes if no 'canvas'.) |

## Output

| Description | Output Type |
| ------ | ------ |
| The base64 if it is converted, if it fails then 'false'. | Text/Boolean |