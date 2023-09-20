# findIndex

## Description

It searches for a specific element in an array and returns the index of the first occurrence of that element. If the element is not found, it returns -1.

## Input / Parameter
| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| string | The array/list where in the search would be done. | Array/List | - | - | Yes |
| find | The value to find in the array/list. | Any | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the index of the first occurrence and if it not found, it returns -1. | Number |

## Callback

N/A

## Video

Coming soon.

## Example

The user wants to get the index of character "H" in a passed string.
<br />

### Step

1. Call the function `console`. Call the function `findIndex` inside the `value` parameter of the `console` function.
    <br />
    string: aBcDeFgHiJ<br />
    find: H
    
   ![](../findIndex/findIndex-step-1.png?raw=true)

   ![](../findIndex/findIndex-step-2.png?raw=true)

### Result

The console should return '7', the index of 'H' in the string.

## Links