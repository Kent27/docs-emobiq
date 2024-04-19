# List.removeLast

## Description

Removes the last element in a list.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| data | The list to be updated. | List | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the updated list. | List |

## Example

In this example, we will remove the last element in a list and print the updated list in the console.

### Steps

1. Call the function `List.removeLast` inside the `Log.write` function.
2. Then call the function `Conversion.toList` inside the `List.removeLast` function.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./removeLast-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The console will print `[3, 1]`.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./removeLast-result-1.png"
        style="width: 35%; padding: 5px;"/>
    </div>

## Links

### Related Information

See also:

- Functions
    - [Conversion.toList](/document/client/2-5-actions-and-visual-logic/action-reference/react-native/Conversion/toList/toList.md)