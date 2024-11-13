# Component.setValue

## Description

Allows users to set a value to a component.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component. | String/Text | - | - | Yes |
| value | The value to be set for the component. | String/Text | - | - | Yes |

## Output

Note: The component will be updated to show the value that has been set to it.

## Example

In this example, we will set the value of a text input component, where once it is clicked the value of the text input component will change to say "This is the Input Box!" 

### Steps

1. First, we drag a button and a text input onto the canvas.
2. Select the button and under the 'Actions' tab, drag the `Component.setValue` into the flow for the button. 

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setValue-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

3. Under the inspector for this function, select the component whose value you would be changing, which in this example is `InputBox`.
4. Enter the new value to display. 

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setValue-step-2.png"
        style="width: 40%; padding: 5px;"/>
    </div>

### Result

1. Save and preview your app. 
2. Now when you click the button, it will set the component value of InputBox to 'This is the Input Box!'

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setValue-result-1.png"
        style="width: 40%; padding: 5px;"/>
    </div>

## Links

### Related Information

See also:

- Functions
    - [Component.getValue](/document/client/gitbook/2-5-actions-and-visual-logic/action-reference/react-native/Component/getValue/getValue.md)