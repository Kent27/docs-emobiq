# Logic.and

## Description

'and' operator is a boolean operator that returns true if both operands are true and returns false otherwise. 

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| value1 | The first boolean value to check. | Boolean | - | - | Yes |
| value2 | The second boolean value to check. | Boolean | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns true if both operators are true, returns false otherwise. | Boolean |

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to check if value 1 and value 2 are both true and return the result in the console.
</br>

### Step

1. Call the function `Logic.and` inside the `Log.write` function.
    </br>
    value1 : greater (value1:  3000 and value2:  1100)<br />
    value2 : true<br />

2. Call the function `Logic.greaterThan` inside the parameter `value1`.
    </br>
    value1 : 3000<br />
    value2 : 1100<br />

    ![](./and-step-1.png)

    ![](./and-step-2.png)

### Result

The console will print 'true' since `value1` will return 'true' (3000 is greater than 1100) which matches the input for `value2` (true).

## Related Information