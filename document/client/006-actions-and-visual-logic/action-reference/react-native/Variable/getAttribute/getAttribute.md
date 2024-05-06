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

## Example

In this example, we will use a value of an attribute from global variable which had been declared.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Assuming you have followed the "Variable.setAttribute" fuction in help document, call the function.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./getAttribute-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. If the specified global variable attribute has previously been set (see [`setAttribute`](./setAttribute)), the function will return the variable attribute's value ("Johnny" in this example).

2. If the specified global variable attribute does not exist, the function will return the value in `defaultValue`.

## Links

### Related Information

See also 

- Functions
    - [Variable.setAttribute](/document/client/2-5-actions-and-visual-logic/action-reference/react-native/Variable/setAttribute/setAttribute.md)