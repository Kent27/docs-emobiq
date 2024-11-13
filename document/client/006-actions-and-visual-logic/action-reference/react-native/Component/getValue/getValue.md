# Component.getValue

## Description

Returns the value of the component specified by the user. The component value can be displayed in another component using the [`setValue`](./setValue) function.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component that the value is retrieved from. | String/Text | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the value of the component specified. | String/Text |


## Example

In this example, we will get the component value of an input field using `Component.getValue` and print it to the console. 

### Steps

1. First we drag an input box onto the page. We will name it "InputBox" with the value "This is an input field".

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./getValue-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

2. We want to get the value of "InputBox" and display it in the browser console with the help of the `Console.write` helper function. 
3. Drag `Component.getValue` into the event flow, and specify the name of the component, which in this case is "InputBox".

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./getValue-step-2.png"
        style="width: 75%; padding: 5px;"/>
    </div>


### Result

1. The value of "InputBox" will be displayed in the browser console.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./getValue-result-1.png"
        style="width: 30%; padding: 5px;"/>
    </div>

## Links

### Related Information

See also:

- Functions
    - [Component.setValue](/document/client/gitbook/2-5-actions-and-visual-logic/action-reference/react-native/Component/setValue/)