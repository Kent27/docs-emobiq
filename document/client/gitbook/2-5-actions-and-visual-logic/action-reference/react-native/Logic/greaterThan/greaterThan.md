# Logic.greaterThan

## Description

The greater than comparison operator. It checks whether the first value is greater than the second value. The result will return boolean values, true or false.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| value1 | The first value to check. | Number | - | - | Yes |
| value2 | The second value to check against. | Number | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns true if the first value is greater than the second value, returns false otherwise. | Boolean |

## Example

In this example, we will check if the first value passed is greater than the second value passed and print the result in the console.

### Step

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Logic.greaterThan` inside the `Log.write` function.
    <br />
   value1 : 18<br />
   value2 : 10<br /><br />
    ![](./greaterThan-step-1.png)
    <br />

### Result

1. The console will return `true`.
