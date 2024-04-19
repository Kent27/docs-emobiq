# Math.power

## Description

Exponentiation of two numbers. The output will return the base number raised to the power (or exponent) passed.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| base | The base number to be raised. | Number | - | - | Yes |
| exponent | The number of powers to raise the base number to. | Number | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the base number raised to the power specified. | Number |

## Example

In this example, we will find the value of a base number raised to power specified and print it in the console.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Math.power` inside the `Log.write` function.
3. Enter the values for the base and the power.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./power-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The console will print `8`.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./power-result-1.png"
        style="width: 10%; padding: 5px;"/>
    </div>
