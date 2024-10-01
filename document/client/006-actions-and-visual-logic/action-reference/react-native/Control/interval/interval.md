# Control.interval

## Description

Executes a function continuously with the specified interval between each execution. 

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| delay | The duration between each run. (In milliseconds)  | Number | 0 | - | Yes |
| timeout | The duration the output appears for. (In milliseconds)   | Number | 0 | - | Yes |
| persistent | Interval is repeated outside current page or not.  | Boolean | false | - | No |

## Output

The function will return true if it ran successfully.

## Callback

The action performed if the condition is true.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Control.interval` function to the event flow.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./interval-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

2. Call the function `Control.interval`. Enter the parameters of the `Control.interval` function.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./interval-step-2.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result
1. The function will return true if interval executed.