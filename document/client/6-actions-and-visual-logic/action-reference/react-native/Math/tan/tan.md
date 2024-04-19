# Math.tan

## Description

Get the tangent of an angle, in radians. The output will return any real number.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| value | The number to return the tangent of. | Number | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the tangent of an angle. | Number |

## Example

In this example, we will get the tangent of a value and print it in the console.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Math.tan` inside the `Log.write` function.
3. Enter the value to get the tangent of.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./tan-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The console will print the tangent of the value passed.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./tan-result-1.png"
        style="width: 25%; padding: 5px;"/>
    </div>
