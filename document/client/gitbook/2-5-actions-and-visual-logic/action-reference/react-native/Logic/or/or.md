# Logic.or

## Description

'or' operator is a boolean operator that returns true if either operand is true and returns false otherwise. 

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| value1 | The first boolean value to check. | Boolean | - | - | Yes |
| value2 | The second boolean value to check. | Boolean | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns true if either operator is true, returns false otherwise. | Boolean |

## Example

In this example, we will check if either of the values passed is true and print the result in the console.
</br>

### Step

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Logic.or` inside the `Log.write` function.
    </br>
    value1 : `greaterThan` function<br />
    value2 : false<br />

![](./or-step-1.png)

3. Call the function `Logic.greaterThan` inside the parameter `value1`.
    </br>
    value1 : 3000<br />
    value2 : 1100<br />

![](./or-step-2.png)

### Result

1. The console will print `true` since `value1` will return 'true' (3000 is greater than 1100) although `value2` returns false.