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


The user wants to add padding to a string with maximum length of 10, with the original string at center.
</br>

### Step

1. Call the function.<br/>
    string: AB<br />
    len: 10<br />
    type: center<br />
        
   ![](../../../../document/function/String/padString/padString-step-1.png?raw=true)

### Result

 ![](../../../../document/function/String/padString/padString-result-1.png?raw=true)
 
 (4 spaces added on both of the left & right of "AB", total length of the string is now 10.)



## Links