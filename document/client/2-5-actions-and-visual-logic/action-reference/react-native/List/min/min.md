# min

## Description

Returns the smallest value of the numbers in the passed array.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| value | The array of values to return the smallest value from. | Array/List | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the smallest value in the array. | Number |

## Example

In this example, we will get the smallest of the numbers in a list and print the result in the console.

### Step

1. Drag a `button` component to the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `List.min` inside the `Log.write` function.
3. Then call the function `Conversion.toList` inside the `List.min` function.
4. Enter the values of the list to find the min from.

![](./min-step-1.png)

### Result

1. The console will print the min value of the list.
2. In this example, the value printed will be `1`.

![](./min-result-1.png)