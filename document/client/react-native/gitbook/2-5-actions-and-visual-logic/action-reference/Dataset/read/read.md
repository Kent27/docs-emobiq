# read

## Description

Read the data from a dataset.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | Name of the dataset that is created in services. | Text | - | - | Yes |
| fields | Will contain a single object, or a list of one (1) or more objects which consist of: dataset, field, title. | Object | - | - | - |
| join | Join filters to be applied, which consist of: type, dataset, filter. | Object | - | - | - |
| filter | Filters to be applied, which consist of: dataset, field, operator, value, dataset1, field1, dataset2, field2. | Object | - | - | - |
| sort | Will contain a single object, or a list of one (1) or more objects which consist of: dataset, field, order. | Object | - | - | - |
| limit | Number of data that will be returned. | Number | - | - | - |
| page | Pagination number. | Number | - | - | - |
| extra | extra parameter to pass into callback. | Text | - | - | - |

## Output

Formatted Result

## Callback

### callback

The function to be executed when the read runs successfully.

### errorCallback

The function to be executed when the read runs unsuccessfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to read `Local Table` data from their local storage, (this example will only works after the user has created the data using `Dataset.insert` function).

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](./read-step-1.png) | Make sure the `Local Table` component that's being used in `Dataset.insert` function example is exist and filled on the services panel in the service page. For `fields` field value add `name`and `title` as object key with Text type. |
| 2. | ![](./read-step-2.png) | Drag a button component to a page in the mobile designer. |
| 3. | ![](./read-step-3.png) | Select the event `press` and drag the `Dataset.read` function to the event flow and fill in the parameter. Drag a `Log.write` as `Dataset.read` callback and use input on it's value param type. |
| 4. | ![](./read-step-4.png) | Open the preview and try to press the Button, new data should be added on local storage. |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

Should be able to read the data from local storage.

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links
