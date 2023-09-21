# btPrinterDisconnect

## Description

Disconnects a bluetooth printer from the device.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| timeout | The duration the printer can be idle for before it is disconnected. | String/Text | - | - | Yes |

## Output

N/A

## Callback

### callback

The function to be executed if the printer is disconnected successfully.

### errCallback

The function to be executed if the printer is not disconnected successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user wants to disconnect a printer from their device.

<!-- Share a scenario, like a user requirements. -->

### Steps

1. Call the function `btPrinterDisconnect` in a button component. 

    ![](../btPrinterDisconnect/btPrinterDisconnect-step-1.png?raw=true)

2. Call the function `infoDialog` in the callbacks of the `btPrinterDisconnect` function.

    ![](../btPrinterDisconnect/btPrinterDisconnect-step-2.png?raw=true)

    ![](../btPrinterDisconnect/btPrinterDisconnect-step-3.png?raw=true)

    ![](../btPrinterDisconnect/btPrinterDisconnect-step-4.png?raw=true)

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}?raw=true) -->

### Result

![](../btPrinterDisconnect/btPrinterDisconnect-result-1.jpg?raw=true)

<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links