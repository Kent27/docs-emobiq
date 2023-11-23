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

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to check whether a printer is connected to their device.

<!-- Share a scenario, like a user requirements. -->

### Steps

1. Call the function `btPrinterIsConnected` in a button component. 

    ![](./btPrinterIsConnected-step-1.png)

2. Call the function `infoDialog` in the callbacks of the `btPrinterIsConnected` function.

    ![](./btPrinterIsConnected-step-2.png)

    ![](./btPrinterIsConnected-step-3.png)

    ![](./btPrinterIsConnected-step-4.png)

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

1. Select the printer to check from the combobox. 
    
    ![](../btPrinterIsConnected/btPrinterIsConnected-result-1.jpg)

2. Press the Is Connected button. If the printer is connected to the device, the success infoDialog will appear. If the printer is not connected, the error dialog will appear.

    ![](../btPrinterIsConnected/btPrinterIsConnected-result-2.jpg)

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links