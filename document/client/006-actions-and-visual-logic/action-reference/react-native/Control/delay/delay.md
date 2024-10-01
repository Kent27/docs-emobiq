# Control.delay

## Description

Inserts a delay before executing another function.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| duration | The time before a function is executed. (In milliseconds)  | Number | - | - | Yes |
| persistent | To still execute outside of the current page or not.  | Boolean | False | - | No |
| extra | The stored value that is passed to all the callbacks. | Any | - | - | No |

## Output

Will return true if executed.

## Callback

### yesCallback

The callback will return all functions under.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Control.delay` function to the event flow.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./delay-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>
2. Call the function `Logic.equal` in the `condition` parameter of the function. Enter the parameters of the `Logic.equal` function.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./delay-step-2.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result
1. The function will return true if delay executed.
