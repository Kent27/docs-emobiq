# remove

## Description

Remove the data from a dataset.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | Name of the dataset that is created in services. | Text | - | - | Yes |
| filter | Filters to be applied, which consist of: dataset, field, operator, value, dataset1, field1, dataset2, field2. | Object | - | - | - |
| extra | extra parameter to pass into callback. | Text | - | - | - |

## Output

Formatted Result

## Callback

### callback

The function to be executed when the remove runs successfully.

### errorCallback

The function to be executed when the remove runs unsuccessfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to remove an item from `Local Table` data from their local storage, (this example will only works after the user has created the data using `Dataset.insert` function).

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](./remove-step-1.png) | Make sure the `Local Table` component that's being used in `Dataset.insert` function example is exist and filled on the services panel in the service page. |
| 2. | ![](./remove-step-2.png) | Drag a button component to a page in the mobile designer. |
| 3. | ![](./remove-step-3.png) | Select the event `press` and drag the `Dataset.loadData` function to the event flow and fill in the parameter. |
| 4. | ![](./remove-step-4.png) | Open the preview and try to press the Button, data should be removed from local storage. |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

Should be able to remove the data from local storage.

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links
