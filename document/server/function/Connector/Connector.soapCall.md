# Connector.soapCall

## Description

Performs a SOAP API call using a SOAP Connector.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| connector | The Rest Connector to be used. | Text  | - | - | Yes |
| header | An object or a list of objects of the SOAP header that will contain arbitrary key-value pairs to be sent as part of the request. | List / Object | - | - | No |
| mimeHeader | The key-value pair of MIME headers (equivalent to HTTP headers) to be sent along with the request. | Object | - | - | No |
| action | The name of the SOAP action to be called. | Text | - | - | Yes |
| body | The content of the SOAP body.. | Object | - | - | No |
| attachment | The map of the key to the file path for attaching files to upload along with the body. | Object / List | - | - | No |
| actionNamespace | The namespace of the SOAP action to be invoked. | Text | - | - | No |
| sendAsMtom | To enable or disable MOM support to send the request. | Boolean | false | true, false | No |
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
| Returns an object with the information of the SOAP call. | Object |

#### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| value | The value returned after the function has been executed. | Object |

### errorCallback

The action performed if this function runs successfully.

| Description | Output Type |
| ------ | ------ |
| Returns an object with the information of the SAOP call. | Object |

#### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| errorMessage | The error message for unsuccessful SOAP call. | Text |
| fault | The fault associated with the error. | Object |

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