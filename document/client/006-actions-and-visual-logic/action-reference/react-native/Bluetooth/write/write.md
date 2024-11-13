# Bluetooth.write

## Description

Sends data to a Bluetooth device.

## Input / Parameter


| Name | Description        | Input Type | Default | Options | Required |
|------|--------------------|------------|---------|---------|----------|
| data | The data to write. | Text       | -       | -       | Yes      |


## Output

| Description                        | Output Type |
|------------------------------------|-------------|
| Returns the formatted information. | Object      |

## Example

In this example, we will attempt to write data to currently active Bluetooth device.
0e sure to connect it first using `Bluetooth.connect`

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button.
2. Add `Bluetooth.write` function, filling up the necessary parameter.
3. Continue to add `Log.write` just under the function, for each of the callbacks available, that is YES (`callback`) and NO (`errorCallback`)

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./write-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. When running the app on Android device, connect it to a computer, and run `adb logcat` on the terminal on that computer
2. Trigger the button press, and observe the output produced by `Log.write` on the terminal.
3. The output will show `true` if the device is connected, or an error message otherwise.


## Links

### Related Information
