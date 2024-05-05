# Device.captureAudio

## Description

Activates the voice recording UI to capture audio.

## Input / Parameter

N/A

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| success | Boolean value to denote whether the function was executed successfully. | Text |
| message | The message to print. | Text |
| data | Any additional message or data to print. | Text |

## Callback

### callback

The function to be executed when the voice recording is generated successfully.

### errorCallback

The function to be executed when the voice recording is not generated successfully.

## Example

In this example, we will create a voice recording using a mobile device and print the audio file path in the console.

### Steps

1. Drag a button component to a page in the mobile designer. Select the event `press` and drag the `Device.captureAudio` function to the event flow.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./captureAudio-step-1.png"
        style="width: 50%; padding: 5px;"/>
    </div>

2. Drag the function to be executed if the audio recording is successful or failed to the node below the function. In this example, we are using the `Log.write` function. Fill in the parameters of the function.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./captureAudio-step-2.png"
        style="width: 70%; padding: 5px;"/>
    </div>

### Result

1. The path of the audio file will be shown in the console.
