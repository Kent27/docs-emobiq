﻿# Math.multiply

## Description

Multiplication of two numbers. The output will return the product of the two numbers.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| value1 | The first number to multiply. | Number | - | - | Yes |
| value2 | The second number to multiply. | Number | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the product of the two values. | Number |

## Example

In this example, we will multiply two values and print the result in the console.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Math.multiply` inside the `Log.write` function.
3. Enter the values to be multiplied.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./multiply-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The console will print `12`.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./multiply-result-1.png"
        style="width: 10%; padding: 5px;"/>
    </div>