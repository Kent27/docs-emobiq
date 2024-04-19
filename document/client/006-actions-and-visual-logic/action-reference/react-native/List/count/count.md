# List.count

## Description

Counts the number of elements in a list.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| data | The list of elements to count. | List | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the total number of the elements in the list. | Number |

## Example

In this exmaple, we will count the number of elements in a list and print the result in the console.

### Step

1. Call the function `List.count` inside the `Log.write` function.
2. Then call the function `Conversion.toList` inside the `List.count` function.
3. Enter the data inside the `Conversion.toList` function. In this example, we will enter "3, 1, 5".

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./count-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The console will print the number of elements in the list. 
2. In this example, the value printed will be `3`.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./count-result-1.png"
        style="width: 10%; padding: 5px;"/>
    </div>

## Links

### Related Information

See also:

- Functions
    - [Conversion.toList](/document/client/2-5-actions-and-visual-logic/action-reference/react-native/Conversion/toList/toList.md)