# canvasToDataURL

## Description

Converts a component to base64.

Note: Not all components are supported, as of now only the following are supported:

- Signature
- Barcode
- QRCode

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| canvas | The name of the component. | String/Text | - | - | Yes |
| componentId | The id of the component. | String/Text | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| The base64 if it is converted, if it fails then 'false'. | Text/Boolean |