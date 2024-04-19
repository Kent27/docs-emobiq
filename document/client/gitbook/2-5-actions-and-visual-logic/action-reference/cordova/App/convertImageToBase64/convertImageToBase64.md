# convertImageToBase64

## Description

Converts an image to base64 format.

### Platform Supported

- Mobile
- Web

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| image | The image to be converted, it can be a asset icon name, local file path or url. If the image is a url must not block [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS). | Text/List | - | - | Yes |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns 'true' if the image was passed and if not it will return 'false'. | Boolean |

## Callback

### callback

The function to be executed when the image is successfully converted to base64 format.

#### Scenario 1

There is no parameter 'extra'.

| Description | Output Type |
| ------ | ------ |
| The base64 of the image, it will return text or list based on the parameter 'image' passed.  | Text/List |

#### Scenario 2

There is a parameter 'extra'.

| Description | Output Type |
| ------ | ------ |
| Contains the result and extra of the function. | Object |

##### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| data | The base64 of the image, it will return text or list based on the parameter 'image' passed. | Text/List |
| extra | The extra value. | Any |