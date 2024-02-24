# Variable.get

## Description

Returns the value of a global variable.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| name | The name of the variable. | String/Text | - | - | Yes |
| defaultValue | The default value of the variable. | String/Text | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the value of the global variable if there is a value, returns the `defaultValue` value otherwise. | String/Text |

## Callback

N/A

## Video

## Example

### Steps

1. Drag the `Variable.get` function into the event flow panel. (*Note: The `Log.write` function is used here for ease of demostrating the output.)

2. Specify the variable name that you would like to access.

![](./getVar-step-1.png)


### Result

| Variable exists | Variable does not exist | 
| ---- | ---- | 
| If the specified global variable has previously been set (see [`set`](./set)), the function will return the variable's value: ("1.0.0" in this example) <br /> ![](./getVar-step-2.png) | If the specified global variable does not exist, the function will return the value in `defaultValue`:  <br /> ![](./getVar-step-3.png) |

## Related Information

* See also `Variable.set`