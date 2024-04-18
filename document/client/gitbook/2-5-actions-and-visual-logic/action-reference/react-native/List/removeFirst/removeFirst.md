# List.removeFirst

## Description

Removes the first element in a list.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| data | The list to be updated. | List | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the updated list. | List |

## Example

In this example, we will remove the first element in a list and print the updated list in the console.

### Steps

1. Call the function `List.removeFirst` inside the `Log.write` function.
2. Then call the function `Conversion.toList` inside the `List.removeFirst` function.

![](./removeFirst-step-1.png)

### Result

1. The console will print `[1, 5]`.

![](./removeFirst-result-1.png)