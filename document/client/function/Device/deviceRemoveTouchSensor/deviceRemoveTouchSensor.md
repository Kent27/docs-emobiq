# deviceRemoveTouchSensor

## Description

Removes the touch sensor feature in a mobile device.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| key | The key in the device keychain. | String/Text | - | - | Yes |

## Output

N/A

## Callback

### callback

The function to be executed if touch sensor feature is removed successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user wants to remove the touch sensor feature of their mobile device.

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](../deviceRemoveTouchSensor/deviceRemoveTouchSensor-step-1.png?raw=true) | Drag a button to a page in the mobile designer. Select the event `click` for the button and drag the function `deviceRemoveTouchSensor` to the event flow. |
| 2. | ![](../deviceRemoveTouchSensor/deviceRemoveTouchSensor-step-2.png?raw=true) | Fill in the parameters of the function.  |
| 3. | ![](../deviceRemoveTouchSensor/deviceRemoveTouchSensor-step-3.png?raw=true) | Drag the function to be executed when the touch sensor is removed successfully. In this example, we are using the `infoDialog` function. |
| 4. | ![](../deviceRemoveTouchSensor/deviceRemoveTouchSensor-step-4.png?raw=true) | Fill in the parameters of the function.  |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}?raw=true) -->

### Result

When the button is pressed, the infoDialog will appear to confirm that the touch sensor has been removed.

<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links