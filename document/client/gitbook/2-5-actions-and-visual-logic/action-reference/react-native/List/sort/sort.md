# List.sort

## Description

Sorts the elements in a list in ascending or descending order.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| data | The list of elements to be sorted. | List | - | - | Yes |
| descending | Sorts the elements in ascending order if 'false', sorts in descending order if 'true'. | Boolean | false | true, false | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the sorted list. | List |

## Callback

N/A

## Video

Coming Soon.

## Example

The user wants to sort a list and print the updated list in the console.
</br>

### Step

1. Call the function `List.sort` inside the `Log.write` function, and then Call the function `Conversion.toList` inside the `List.sort`. When `descending` is not specified it will be false by default.
    </br>

    ![](./sort-step-1.png)

### Result

The console will print `[1, 3, 5]`.

## Related Information