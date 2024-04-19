# Signature.clear

## Description

A function to clear the canvas and allow users to redraw the signature.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the signature component. | Text | - | - | Yes |

## Output

Note: The signature component will be updated and clear the canvas.

## Example

In this example, we will clear the current signature canvas.

### Steps

1. Drag a `signature` and `button` component into the canvas and open the `Action` tab. Label the button "Clear".

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clear-step-1.png"
        style="width: 50%; padding: 5px;"/>
    </div>

2. Select the `press` event of the button component and drag the `Signature.clear` function to the event flow. Select the signature component that should be cleared when this button is clicked.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clear-step-2.png"
        style="width: 40%; padding: 5px;"/>
    </div>

3. Save and preview the app. Sign on the signature component canvas, then click the 'Clear' button to clear the canvas.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clear-step-3.png"
        style="width: 50%; padding: 5px;"/>
    </div>

### Result

1. The canvas of the signature component specified in the `component` parameter will be cleared.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clear-result-1.gif"
        style="width: 40%; padding: 5px;"/>
    </div>

## Links

### Related Information

See also:

- Components
    - [Signature]()