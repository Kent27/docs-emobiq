# btPrinterConnect

## Description

Connects a bluetooth printer to the device.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| printerID | The id of the printer to connent. | String/Text | - | - | Yes |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

N/A

## Callback

### callback

The function to be executed if the printer is connected successfully.

### errCallback

The function to be executed if the printer is not connected successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user wants to connect a printer to their device.

<!-- Share a scenario, like a user requirements. -->

### Steps

1. Drag a combobox and button component to a page in the mobile designer. Call the function `btPrinterConnect` in the button component. 

    ![](../btPrinterConnect/btPrinterConnect-step-1.png?raw=true)

2. Call the function `componentValue` in the `printerId` parameter of the `btPrinterConnect` function. Select the combobox component in the `component` parameter of the `componentValue` function to view the printers connected.

    ![](../btPrinterConnect/btPrinterConnect-step-2.png?raw=true)

    ![](../btPrinterConnect/btPrinterConnect-step-3.png?raw=true)

3. Call the function `infoDialog` in the callbacks of the `btPrinterConnect` function.

    ![](../btPrinterConnect/btPrinterConnect-step-4.png?raw=true)

    ![](../btPrinterConnect/btPrinterConnect-step-5.png?raw=true)

    ![](../btPrinterConnect/btPrinterConnect-step-6.png?raw=true)

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}?raw=true) -->

### Result

If the printer is connected to the device successfully, it will show in the combobox and the success infoDialog will appear. If the printer is not connected successfully, it will not show in the combobox and the error dialog will appear.

<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links