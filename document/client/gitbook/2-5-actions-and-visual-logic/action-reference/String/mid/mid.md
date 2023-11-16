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

The user wants to get a specific number of characters from a string, starting from the index specified.</br>

### Step

1. Call the function `console`. Call the function `mid` inside the `value` parameter of the `console` function.
    </br>
    string: ABCDEFGHIJ<br />
    start: 1<br />
    length: 3<br />
    
    ![](./mid-step-1.png)

    ![](./mid-step-2.png)

### Result

![](./mid-result-1.png)

## Links