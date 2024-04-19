# List.insertFirst

## Description

Inserts an element to the front of a list.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| data | The list to be updated. | List | - | - | Yes |
| value | The element to be added to the list. | Any | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the updated list. | List |

## Example

In this example, we will insert a value in the first index of a list and print the result in the console.

### Step

1. Call the function `List.insertFirst` inside the `Log.write` function
2. Then call the function `Conversion.toList` inside the `List.insertFirst` function.

![](./insertFirst-step-1.png)

### Result

1. The console will print `[1,3,1,5]`.

![](./insertFirst-result-1.png)