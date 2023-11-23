# getPreviousPage

## Description

Returns the name of the page the user was on before the current page.

## Input / Parameter

N/A

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the name of the previous page. | String/Text |

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to get the name of the previous page they were on.

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](./getPreviousPage-step-1.png) | Drag a button to a page in the mobile designer. Select the event `click` for the button and drag the `gotoPage` function to the event flow. |
| 2. | ![](./getPreviousPage-step-2.png) | Fill in the parameters of the function. |
| 3. | ![](./getPreviousPage-step-3.png) | Drag the `console` function to the node below the `gotoPage` function. |
| 4. | ![](./getPreviousPage-step-4.png) | Select the `function` parameter input type for the value parameter. |
| 5. | ![](./getPreviousPage-step-5.png) | Drag the `getPreviousPage` function to the node in the subflow. |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

When the button is pressed, the page will navigate to pgWelcome and the console will show the name of the previous page.

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links