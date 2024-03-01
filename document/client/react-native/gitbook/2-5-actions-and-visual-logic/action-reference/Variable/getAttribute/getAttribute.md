# Variable.getAttribute

## Description

Retrieves value from an attribute of an object variable in the application's local variable pool.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| name | The variable's identifier containing the object. | Text | - | - | Yes |
| attribute | The attribute name of the object variable to retrieve value from. | Text | - | - | Yes |
| defaultValue | The default value to be used if the attribute does not exist or does not contain a value. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| The stored variable's value from the attribute, or null if the value does not exist, variable is not an object and default value is not supplied. | Any |

## Callback

N/A

## Video

Coming Soon.

## Example

The user wants to use a value of an attribute from global variable which had been declared.

### Steps

1. Assuming you have followed the "Variable.setAttribute" fuction in help document, call the function.

    ![](./getVarAttr-step-1.png)
    ![](./getVarAttr-step-2.png)

### Result

In console, user can see the string `Johnny`. If user variable `vObject` have no value, it will display `unknown`.

## Related Information