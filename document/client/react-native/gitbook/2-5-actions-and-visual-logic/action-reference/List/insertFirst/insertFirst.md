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

## Callback

N/A

## Video

Coming Soon.

## Example

The user wants to insert a value in the first index of a List and print the result in the console.
</br>

### Step

1. Call the function `List.insertFirst` inside the `Log.write` function, and then Call the function `Conversion.toList` inside the `List.insertFirst`.
    </br>

    ![](./insertFirst-step-1.png)

### Result

The console will print `1,3,1,5`.

## Related Information