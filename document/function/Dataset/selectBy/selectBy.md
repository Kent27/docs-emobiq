# selectBy

## Description

Retrieves the specified field from a local table.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the local table to select the records from. | String/Text | - | - | Yes |
| by | The name of the field to select the records from. | String/Text | - | - | Yes |
| operator | The operator to use to determine the records to select. | String/Text | = | =, >, <, >=, <=, !=, like, ilike | No |
| value | The records to be selected from the local table. | String/Text | - | - | Yes |
| first? | ? | String/Text | - | - | No |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the list of records selected from the local table. | Array/List |

## Callback?

### callback

The function to be executed if the specified records are selected successfully.

### errCallback

The function to be executed if the specified records are not selected successfully.

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