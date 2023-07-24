# filterData

## Description

Retrieves the data that has been filtered with a specific field name from a local table.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the local table to be filtered. | String/Text | - | - | Yes |
| or? | Filter by all criterias or by any one. | Boolean | false | true, false | No |
| criteria1 | The first criteria to filter the dataset by. | Object | - | - | Partial (Yes if none of the other criterias have value.) |
| criteria2 | The second criteria to filter the dataset by. | Object | - | - | Partial (Yes if none of the other criterias have value.) |
| criteria3 | The third criteria to filter the dataset by. | Object | - | - | Partial (Yes if none of the other criterias have value.) |
| criteria4 | The fourth criteria to filter the dataset by. | Object | - | - | Partial (Yes if none of the other criterias have value.) |
| criteria5 | The fifth criteria to filter the dataset by. | Object | - | - | Partial (Yes if none of the other criterias have value.) |

__\* Note:__ At least one field from criteria1 to criteria5 must have value in order for this function to work.

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the list of filtered records from the local table. | Array/List |

## Callback?

### callback

The function to be executed if the local table is filtered successfully.

### errorCallback

The function to be executed if the local table is not filtered successfully.

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