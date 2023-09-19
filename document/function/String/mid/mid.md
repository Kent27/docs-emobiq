# mid

## Description

Extract a specified number of characters from any side of a text.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| string | The value where the extraction would happen. | String/Text | - | - | Yes |
| start | The character count position where to start to extraction. The counting starts at 0. | Number | 0 | - | Yes |
| length | The number of characters to extract. | Number | 0 | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the extracted text. | String/Text |

## Callback

N/A

## Video

Coming soon.


## Example


The user wants to get a specified number of characters from a string.</br>

### Step

1. Call the function.
    </br>
    string: ABCDEFGHIJ<br />
    start: 1<br />
    length:2<br />
    
    ![](../../../../document/function/String/mid/mid-step-1.png?raw=true)

### Result

"BC" (index in an array start from 0, therefore when the user specify start at 1, it would start from the second character of a string)



## Links