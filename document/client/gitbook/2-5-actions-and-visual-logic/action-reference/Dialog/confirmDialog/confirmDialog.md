# confirmDialog

## Description

Displays a dialog box (modal) that asks for confirmation from the user.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| title | The title of the dialog box. | String/Text | - | - | Yes |
| content | The message to be shown in the dialog box. | String/Text | - | - | Yes |
| okCaption | The label for the 'OK' button. | String/Text | - | - | No |
| cancelCaption | The label for the 'Cancel' button. | String/Text | - | - | No |

## Output

N/A

Note: A modal will pop up which displays the parameters specified by the user.

## Callback

### okCallback

Functions to be executed when the user clicks the 'OK' button.

### cancelCallback

Functions to be executed when the user clicks the 'Cancel' button.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to display a dialog box to ask for confirmation from the end user.

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](./confirmDialog-step-1.png) | Drag a button to a page in the mobile designer. Select the event `click` for the button and drag the `confirmDialog` function to the event flow. |
| 2. | ![](./confirmDialog-step-2.png) | Fill in the parameters of the function. |
| 3. | ![](./confirmDialog-step-3.png) | Drag the function to be executed when the OK button is pressed. In this example, we are using the `gotoPage` function. |
| 4. | ![](./confirmDialog-step-4.png) | Fill in the parameters of the function. |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

| No. | Description |
| ------ | ------ |
| ![](./confirmDialog-result-1.png) | When the button is pressed, the confirmDialog modal appears. When 'Proceed' button is pressed on the modal, the page navigates to pgWelcome. |

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links