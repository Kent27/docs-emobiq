# left

## Description

Extract a specified number of characters from the left side of a text.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| string | The value where the extraction would happen. | String/Text | - | - | Yes |
| length | The number of characters to extract. | Number | 0 | - | Yes |
| byLanguageFormat | To follow the language format. Usually this matters for languages that doesn't use alphabet. | Boolean | false | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the extracted text. | String/Text |

## Callback

N/A

## Video

Coming soon.

## Example

The user wants to display a specified number of characters from the left hand side of a string.

### Step

1. Call the function `console`. Call the function `left` inside the `value` parameter of the `console` function.<br />
    string: 123456789<br />
    length : 6<br />

   ![](./left-step-1.png)

   ![](./left-step-2.png)

### Result

![](./left-result-1.png)

## Links