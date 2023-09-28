# Dataset.remove

## Description

Removes certain data from a dataset.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the dataset that is created in Services. | Text | - | - | Yes |
| filter | The filters to be applied. | FilterFormat | - | - | No |
| extra | The stored value that is passed to all the callbacks. | Any | - | - | No |

### FilterFormat (Object)

The format used for filtering in the parameter `filter`.

| Key | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| operator | Query operators used to filter multiple times. | Text | And | Or, And | No |
| data | Set of rules for another group of queries. | List | - | - | No |

#### data (List)

Will contain a list of one (1) or more objects with the folowing structure (dataset, operator, value) and contain zero (0) or more objects with the same structure (FilterFormat only). This can be another FilterFormat to create grouped queries.

| Key | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The dataset to filter. | Text | - | - | No |
| field | The field to be filtered. | Text | - | - | Yes |
| operator | Operators to be used for specific filtering. | Text | - | Equal, Not_Equal, Is_Null, Is_Not_Null, Greater_Than, Greater_Than_Or_Equal, Less_Than, Less_Than_Or_Equal, Like, Not_Like, In, Not_In, Between, Not_Between | Yes |
| value | The value to perform the query, which depends on the operator. | Any | - | - | No |

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
| Returns a boolean value if data is deleted. | Boolean |

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