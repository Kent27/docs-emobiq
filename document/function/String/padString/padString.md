# padString

## Description

Generates a padded text. A padded text has additional characters added to either its beginning, end, or both sides to achieve a desired length or formatting.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| string | The value to be padded. | String/Text | - | - | Yes |
| len | The length of the new padded text. | Number | 0 | - | Yes |
| type | The location of the 'string' within the new padded text. | String/Text | right | right, left, center | Yes |
| char | The value to use as padding. | String/Text | ' ' | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the padded value. | String/Text |

## Callback

N/A

## Video

Coming soon.

## Example

The user wants to add padding to a string with maximum length of 10, with the original string at the center.
</br>

### Step

1. Call the function `console`. Call the function `padString` inside the `value` parameter of the `console` function.<br/>
    string: AB<br />
    len: 10<br />
    type: center<br />
    char: 1<br />

    ![](../padString/padString-step-1.png?raw=true)

    ![](../padString/padString-step-2.png?raw=true)

### Result

 ![](../padString/padString-result-1.png?raw=true)
 
 There are 4 characters '1' added on both the left & right side of "AB", making the total length of the string 10.



## Links