# loadNext

## Description

Loads the subsequent records in a dataset after loadData function was run.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | Name of the dataset that is created in services. | Text | - | - | Yes |

## Output

Formatted Result

## Callback

### beforeCallback

The function to be executed before this function runs.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to load the next batch of data from `Local Table` to be used in a flatlist component, (this example will only works after the user has created the data using `Dataset.insert` function).

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](./loadNext-step-1.png) | Make sure the `Local Table` component that's being used in `Dataset.insert` function example is exist and filled on the services panel in the service page. |
| 2. | ![](./loadNext-step-2.png) | Drag a button component to a page in the mobile designer. |
| 3. | ![](./loadNext-step-3.png) | Drag a flatlist component to a page in the mobile designer, and drag a label component into the newly created flatlist component. |
| 4. | ![](./loadNext-step-4.png) | Fill the flatlist component property in the page and fill the label component property in the flatlist component, make sure the label component field value match with the key of the data that being stored in the local storage. |
| 5. | ![](./loadNext-step-5.png) | Select the event `press` and drag the `Dataset.loadNext` function to the event flow and fill in the parameter. |
| 6. | ![](./loadNext-step-6.png) | Open the preview and try to press the Button, the flatlist component should display the next batch of data from local storage. |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

Should be able to load the next batch of data from local storage and display it on flalist component.

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links
