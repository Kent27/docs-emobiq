# btPrinterPortList

## Description

Returns a list of all the bluetooth printer ports.

## Input / Parameter

N/A

## Output

N/A

## Callback

### callback

The function to be executed if the printer ports are returned successfully.

### errCallback

The function to be executed if the printer ports are not returned successfully, or when 'btPrinterPortList error: bluetoothClassicSerial plugins not found' is returned.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user wants to connect to view the list of printers available.

<!-- Share a scenario, like a user requirements. -->

### Steps

1. Call the function `btPrinterPortList` in a button component. 

2. Call the function `setComboOptions` in the callback and `infoDialog` in the errCallback of the `btPrinterPortList` function.

    ![](../btPrinterPortList/btPrinterPortList-step-1.png?raw=true)

    ![](../btPrinterPortList/btPrinterPortList-step-2.png?raw=true)

    ![](../btPrinterPortList/btPrinterPortList-step-3.png?raw=true)

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}?raw=true) -->

### Result

1. Press the Generate Printer List button. 
    
2. If the printer list is generated, the printers will be shown in the combobox. If the printer list is not generated, the error dialog will appear.

    ![](../btPrinterPortList/btPrinterPortList-result-1.jpg?raw=true)

<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links