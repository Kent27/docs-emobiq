# Format.number

## Description

Formats a number using certain separators to be read better.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| value | The value to be formatted. | Number | - | - | Yes |
| decimal | The number of decimal places that should be seen. Example: If the input is 5, the value will have 5 decimal place such as, 123.00000. | Number | - | - | No |
| decimalSeparator | The separator for decimals, such as a decimal point. | Text | - | - | No |
| thousandSeparator | The separator for millons and thousands place in values. Example: If the input is ' ', 1000000 will be returned as 1 000 000. | Text | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted number with decimal point and separators where needed. | Text |

## Example

In this example, we will adjust a number's thousand and decimal separator and print the formatted number in the console.

### Step

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Format.number` inside the `Log.write` function.
3. Sample parameters are shown in the picture below.

![](./number-step-1.png)

### Result

1. The console will print the formatted number.

![](./number-result-1.png)