# Component.setOptions

## Description

Allows users to set a value to a component.

## Input / Parameter

| Name         | Description                                                                                                            | Input Type  | Default | Options | Required                       |
|--------------|------------------------------------------------------------------------------------------------------------------------|-------------|---------|---------|--------------------------------|
| component    | The name of the component.                                                                                             | String/Text | -       | -       | Yes, if componentId is not set |
| componentId  | The component ID (for components in FlatList item)                                                                     | String/Text | -       | -       | Yes, if component is not set   |
| data         | The id of the component.                                                                                               | Array/List  | -       | -       | Yes                            |
| valueField   | The name of the attribute from the list of options (from data parameter) to be as the value of the dropdown options.   | String/Text | -       | -       | Yes                            |
| displayField | The name of the attribute from the list of options (from data parameter) to be as the display of the dropdown options. | String/Text | -       | -       | Yes                            |

## Output

| Description                        | Output Type |
|------------------------------------|-------------|
| Returns the formatted information. | Object      |

Note: The component will be updated to show the value that has been set to it.

### Object

| Key     | Description                                                             | Output Type |
|---------|-------------------------------------------------------------------------|-------------|
| success | Boolean value to denote whether the function was executed successfully. | Text        |
| message | The message to print.                                                   | Text        |
| data    | Any additional message or data to print.                                | Text        |

## Example

In this example, we have a button (in blue) that when clicked will populate the dropdown of the component.

### Steps

1. First, we drag a button and a dropdown input onto the Editor.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setOptions-step-1.png"
        style="width: 50%; padding: 5px;"/>
    </div>

2. Select the button and under the 'Actions' tab, drag the `Component.setOptions` into the flow for the button. 

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setOptions-step-2.png"
        style="width: 40%; padding: 5px;"/>
    </div>

3. Under the inspector for this function, select the component whose dropdown you would be populating, which in this example is `Dropdown411`, and then fill in valueField and displayField

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setOptions-step-3.png"
        style="width: 40%; padding: 5px;"/>
    </div>

4. Add the function `Conversion.toList` in the 'data' parameter using the 'function' parameter type.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setOptions-step-4.png"
        style="width: 40%; padding: 5px;"/>
    </div>

5. Then add `Conversion.toObject` inside each parameter of the `Conversion.toList` function. The object must follow valueField and displayField that has been set 

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setOptions-step-5.png"
        style="width: 40%; padding: 5px;"/>
    </div>

### Result

1. Save and preview your app. 
2. Now when you click the button, it will set the dropdown of Dropdown411.

## Links

### Related Information

See also:

- Components
    - [Dropdown]()
