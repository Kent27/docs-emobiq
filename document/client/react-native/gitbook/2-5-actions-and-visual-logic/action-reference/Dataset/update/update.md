# update

## Description

Update the data from a dataset.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | Name of the dataset that is created in services. | Text | - | - | Yes |
| filter | Filters to be applied, which consist of: dataset, field, operator, value, dataset1, field1, dataset2, field2. | Object | - | - | - |
| data | Mapping of key-value pairs of data to replace. | Object | - | - | - |
| extra | extra parameter to pass into callback. | Text | - | - | - |

## Output

Formatted Result

## Callback

### callback

The function to be executed when the update runs successfully.

### errorCallback

The function to be executed when the update runs unsuccessfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to update `Local Table` data from their local storage, (this example will only works after the user has created the data using `Dataset.insert` function).

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](./update-step-1.png) | Make sure the `Local Table` component that's being used in `Dataset.insert` function example is exist and filled on the services panel in the service page. For `fields` field value add `name`and `title` as object key with Text type. |
| 2. | ![](./update-step-2.png) | Drag a button component to a page in the mobile designer. |
| 3. | ![](./update-step-3.png) | Select the event `press` and drag the `Dataset.update` function to the event flow and fill in the parameter, for the `filter` and `data` param change it's type to a function / subflow and put `Conversion.toObject` inside it |
| 4. | ![](./update-step-4.png) | For the `filter` param change it's type to a function / subflow and put `Conversion.toObject` inside it then add `data` as object key, change it's type to a function / subflow and put `Conversion.toObject` inside it. |
| 5. | ![](./update-step-5.png) | Inside `data` subflow put `Conversion.toObject` inside it then add `field`, `operator`, `value` as object key with `name`, `like`, `n%` as it's value respectively. |
| 6. | ![](./update-step-6.png) | For the `data` param change it's type to a function / subflow and put `Conversion.toObject` inside it then add `title` as object key, with `new value` as it's value. |
| 7. | ![](./update-step-7.png) | Open the preview and try to press the Button, data should be updated on local storage. |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

Should be able to update the data from local storage.

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links
