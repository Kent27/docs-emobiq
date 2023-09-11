# Concurrency.spawnThread

## Description

Waits for a series of functions to be run first.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| successCallback | All the functions in threadCallback will need to be completed before successCallback is run. | Any | - | - | No |
| threadCallback | The series of functions to be completed before successCallback can be run. | Any | - | - | No |
| extra | The stored value that is passed to all the callbacks. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| success | Boolean value to denote whether the function was executed successfully. | Text |
| message | The message to print. | Text |
| data | Any additional message or data to print. | Text |

## Callback

### successCallback

The action performed if this function runs successfully.

| Description | Output Type |
| ------ | ------ |
| Returns the successCallback parameter. | Any |

### errorCallback

The action performed if this function runs successfully.

| Description | Output Type |
| ------ | ------ |
| Returns the threadCallback parameter. | Any |

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