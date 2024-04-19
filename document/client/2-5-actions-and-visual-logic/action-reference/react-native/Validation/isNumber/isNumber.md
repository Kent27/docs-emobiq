# Validation.isNumber

## Description

Checks whether the value input is a number.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| value | The value to be checked. | Any | - | - | Yes |

## Output

N/A

## Example

In this example, we will check whether a Number is valid and print the result in the console.

### Step

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Validation.isNumber` inside the `Log.write` function.
3. Enter the value for the number to be validated. In this example, we will enter the value "12".

![](./isNumber-step-1.png)

### Result

1. The console will print `true` since it is a valid Number.