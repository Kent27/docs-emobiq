# Variable.setAttribute

## Description

Stores value into an attribute of an object variable in the application's local variable pool.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| name | The variable's identifier containing the object. | Text | - | - | Yes |
| attribute | The attribute name of the object variable to set value to. | Text | - | - | Yes |
| value | The value to be set for this variable. Can be null. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| success | Boolean value to denote whether the function was executed successfully. | Text |
| message | The message to print. | Text |
| data | Any additional message or data to print. | Text |

## Callback

N/A

## Video

Coming Soon.

## Example

Coming Soon.

### Steps

1. Drag the `Variable.setAttribute` into the flow window. 
2. Create a variable called `vObject` with the attribute `name` that has value `Johnny`
![](./setAttribute-step-1.png)
3. This will create a global variable called `vObject` (if it doesn't exist already) with attribute `name` containing the value `Johnny` that can be accessed by other components or on other pages of your app.

### Result

The value of the attribute `name` of the global variable `vObject` can be accessed by using the `Variable.setAttribute`. 

Using the above flow will display the value `Johnny` in the browser console.

## Related Information