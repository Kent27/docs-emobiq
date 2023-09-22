# btPrinterIsConnected

## Description

Checks whether a printer is connected to the device.

## Input / Parameter

N/A

## Output

N/A

## Callback

### yesCallback

The function to be executed if the printer is connected.

### noCallback

The function to be executed if the printer is not connected.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user wants to check whether a printer is connected to their device.

<!-- Share a scenario, like a user requirements. -->

### Steps

1. Call the function `btPrinterIsConnected` in a button component. 

    ![](../btPrinterIsConnected/btPrinterIsConnected-step-1.png?raw=true)

2. Call the function `infoDialog` in the callbacks of the `btPrinterIsConnected` function.

    ![](../btPrinterIsConnected/btPrinterIsConnected-step-2.png?raw=true)

    ![](../btPrinterIsConnected/btPrinterIsConnected-step-3.png?raw=true)

    ![](../btPrinterIsConnected/btPrinterIsConnected-step-4.png?raw=true)

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}?raw=true) -->

### Result

If the printer is connected to the device, the success infoDialog will appear, otherwise the error infoDialog will appear.

<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links