# Control.clearInterval

## Description

Clears existing interval(s).

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| intervalId | The id of the interval to clear. | Boolean | - | - | Yes |
| all | To clear all intervals or not (only for interval with persistent equals false) | Boolean | false | - | No |

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Control.clearInterval` function to the event flow.
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clearInterval-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

2. Call the function `Control.clearInterval`. Enter the parameters of the `Control.clearInterval` function.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clearInterval-step-2.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The function will clear all interval that has false as persistent value.
