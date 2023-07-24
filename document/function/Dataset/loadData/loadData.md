# loadData

## Description

Loads the data from a local table, staging database or 3rd party connector.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the local table to load data from. | String/Text | - | - | Yes |
| limit | The number of records to be returned from the local table. | Number | - | - | No |
| page | The page number. | Number | - | - | No |
| filter | The filters for the fields and values to retrieve. | Array/List | - | - | Yes |
| orFilter | Additional filters for the fields and values to retrieve. | Array/List | - | - | No |
| order | Sorts the data with the provided details. | Array/List | - | - | No |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the list of records that is loaded. | Array/List |

## Callback?

### callback

The function to be executed if the records are loaded successfully.

### errorCallback

The function to be executed if the records are not loaded successfully.

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