# Math.divide

## Description

Division of two numbers. The output will return the quotient of the two values.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dividend | The number to be divided. | Number | - | - | Yes |
| divisor | The number to divide the first value by. | Number | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the quotient. | Number |

## Example

In this example, we will divide two values and print the result in the console.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Math.divide` inside the `Log.write` function.
3. Enter the values for the dividend and the divisor.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./divide-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The console will print `3`.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./divide-result-1.png"
        style="width: 10%; padding: 5px;"/>
    </div>
