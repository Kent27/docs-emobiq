# infoDialog

## Description

Displays a dialog box (modal) that shows some message set by the user.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| title | The title of the dialog box. | String/Text | - | - | Yes |
| content | The message to be shown in the dialog box. | String/Text | - | - | Yes |
| disableTimer | To disable the timer or not. | Boolean | false | true, false | No |
| timeOut | The duration that the modal appears on the screen for. (1 second = 1000) | Number | - | - | No |
| okCaption | The label for the 'OK' button. | String/Text | - | - | No |
   
## Output

N/A

Note: A modal will pop up which displays the parameters specified by the user.

## Callback

### okCallback

The function to be executed when user clicks on the button in the modal.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user wants to display some information in a dialog box.

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](../infoDialog/infoDialog-step-1.png?raw=true) | Drag a button to a page in the mobile designer. Select the event `click` for the button and drag the `infoDialog` function to the event flow. |
| 2. | ![](../infoDialog/infoDialog-step-2.png?raw=true) | Fill in the parameters of the function. |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}?raw=true) -->

### Result

| No. | Description |
| ------ | ------ |
| ![](../infoDialog/infoDialog-result-1.png?raw=true) | When the button is pressed, the infoDialog modal appears showing the information entered by the user. |

<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links