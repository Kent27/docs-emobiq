# canvasToImage

## Description

Copies the component content to an image component.

Note: Not all components are supported, as of now only the following are supported:

- Signature
- Barcode
- QRCode

## Input / Parameter

| Name | Description | Data Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| canvas | The name of the component to be copied. | Text | - | - | Yes |
| image | The name of the image component to put the data to. | Text | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns 'true' or 'false', if the function was executed successfully. | Boolean |