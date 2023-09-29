# barcodeScanner

## Description

Activates a barcode scanner using the camera of the device.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| showFlipCameraButton | Show flip camera button. Supported on iOS and Android. | Boolean | true | true, false | No |
| showTorchButton | Show torch button. Supported on iOS and Android. | Boolean | true | true, false | No |
| torchOn | Launch with the torch switched on (if available). Supported on Android only. | Boolean | false | true, false | No |
| prompt | Prompt text. Supported on Android only. | String/Text | - | - | No |
| resultDuration | Display scanned text for X ms. 0 suppresses it entirely, default 1500. Supported on Android only. | Number | 500? | - | No |

## Output

<<<<<<< HEAD
N/A
=======
| No | Name | Description | Data Type | Required |
| ------ | ------ | ------ |------ | ------ |
| 1 | callback | Success Callback | functionList | Yes | 
| 2 | errCallback | Error Callback | functionList | Yes | 
>>>>>>> EP-686-server-fixes

## Callback

<<<<<<< HEAD
### callback
=======
- N/A
>>>>>>> EP-686-server-fixes

The function to be executed if the barcode scanner is activated successfully.

<<<<<<< HEAD
### errorCallback

The function to be executed if the barcode scanner is not activated successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user wants to scan a barcode and display the value in a dialog.

<!-- Share a scenario, like a user requirements. -->

### Steps

1. Drag a button to a page in the mobile designer. Select the event click and drag the barcodeScanner function to the event flow.

    ![](../barcodeScanner/barcodeScanner-step-1.png?raw=true)

    ![](../barcodeScanner/barcodeScanner-step-2.png?raw=true)

2. Drag the function to be executed when the barcode scanner is activated successfully. In this example, we are using the infoDialog function. Fill in the parameters of the function.

    ![](../barcodeScanner/barcodeScanner-step-3.png?raw=true)

    ![](../barcodeScanner/barcodeScanner-step-4.png?raw=true)

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}?raw=true) -->

### Result

When the button is pressed, the barcode scanner will be activated. After scanning the barcode, the value will be displayed in a dialog box.

<!-- Explain the output.
=======
- N/A

### Result

- N/A
>>>>>>> EP-686-server-fixes

Format: ![]({image-path}?raw=true) -->

<<<<<<< HEAD
## Links
=======
- N/A

### Notes

- N/A
>>>>>>> EP-686-server-fixes
