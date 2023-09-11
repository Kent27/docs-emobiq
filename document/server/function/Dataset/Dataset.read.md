# Dataset.read

## Description

Reads the data from a dataset.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the dataset that is created in Services. | Text | - | - | Yes |
| fields | The fields to be selected from the dataset. If left blank, all fields will be selected. | Object / List | - | - | No |
| join | The join filters to be applied. | Object / List | - | - | No |
| filter | The filters to be applied. | FilterFormat | - | - | No |
| sort | The order to sort the records by. | Object / List | - | - | No |
| limit | The number of records to be returned. | Number | 15 | - | No |
| page | The pagination number. | Number | - | - | No |
| extra | The stored value that is passed to all the callbacks. | Any | - | - | No |

### fields (Object | List)

Will contain a single object, or a list of one (1) or more objects which consist of

| Key | Description | Input Type | Required |
| ------ | ------ | ------ | ------ |
| dataset | The dataset to select fields from. The default value for the dataset will be the main dataset selected in the ‘dataset’ parameter. | Text | No |
| field | The attribute (field) to be selected. | Text | Yes |
| title | The new title (alias) of the field. | Text | No |

### join (Object | List)

Will contain a single object, or a list of one (1) or more objects (JoinFormat) which consist of

| Key | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| type | The type of table join to execute. | Text | Inner_Join | Inner_Join, Left_Join, Right_Join | Yes |
| dataset | The dataset to join to the main dataset. The default value for the dataset will be the main dataset selected in the ‘dataset’ parameter if left empty. | Text | - | - | No |
| filter | The filters to be applied. | FilterFormat | - | - | Yes |

### sort (Object | List)

Will contain a single object, or a list of one (1) or more objects which consist of

| Key | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The dataset to sort. The default value for the dataset will be the main dataset selected in the ‘dataset’ parameter. | Text | - | - | No |
| field | The attribute (field) of the dataset to sort. | Text | - | - | Yes |
| order | The order to sort the rows in the field by. | Text | Ascending | Ascending, Descending | No |

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
| Returns the list of data read from the dataset. | List |

### errorCallback

The action performed if this function does not run successfully.

| Description | Output Type |
| ------ | ------ |
| Returns an error message. | Text |

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