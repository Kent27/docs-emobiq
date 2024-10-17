# Control.clearInterval

## Description

Clears existing interval(s).

## Input / Parameter

| Name       | Description                                                                    | Input Type | Default | Options | Required |
| ---------- | ------------------------------------------------------------------------------ | ---------- | ------- | ------- | -------- | 
| intervalId | The id of the interval to clear.                                               | Boolean    | -       | -       | Yes      |
| all        | To clear all intervals or not (only for interval with persistent equals false) | Boolean    | false   | false, true | No       |

## Output

Returns formatted information. 

## Example

In this example, we will clearInterval by interval id.

__\* Note:__ Must have working `Control.interval` function with it's interval id in order for this function to work.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Control.clearInterval` function to the event flow.
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clearInterval-step-1.png"
        style="width: 60%; padding: 5px;"/>
    </div>

2. Put a `Log.write` function inside the event flow and change the param type to function.
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clearInterval-step-2.png"
        style="width: 60%; padding: 5px;"/>
    </div>

3. Put function `Control.clearInterval` inside `Log.write` function. Enter the parameters of the `Control.clearInterval` function.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clearInterval-step-3.png"
        style="width: 60%; padding: 5px;"/>
    </div>

### Result

1. The function will clear interval that has '123' as the id and this example will return true upon clearing.
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clearInterval-result.png"
        style="width: 100%; padding: 5px;"/>
    </div>