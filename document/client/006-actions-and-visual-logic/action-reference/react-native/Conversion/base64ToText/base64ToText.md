# Conversion.base64ToText

## Description

Decode an encoded base64 string.

## Input / Parameter

| Name  | Description                                             | Input Type | Default | Options | Required |
| ----- | ------------------------------------------------------- | ---------- | ------- | ------- | -------- |
| value | The text to be decoded.       | Text  | -       | -       | Yes      |

## Output

| Description                                   | Output Type |
| --------------------------------------------- | ----------- |
| Returns the decoded text.        | Object      |

## Example

In this example, we will convert a base64 to string and print the result in the console.

### Steps

1. Drag a `Button` component into the service page that will trigger the Base64 decoding action.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./base64ToText-step-1.png"
        style="width: 50%; padding: 5px;"/>
    </div>

2. Drag `Log.write` to event flow and put `Conversion.base64ToText` inside the function parameter.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./base64ToText-step-2.png"
        style="width: 50%; padding: 5px;"/>
    </div>

3. Drag the `Conversion.base64ToText` function to the `Log.write` event function. Fill in the parameter with the Base64 encoded text or list to be converted.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./base64ToText-step-3.png"
        style="width: 70%; padding: 5px;"/>
    </div>

### Result

1. Upon pressing the button, the Base64 encoded will be decoded back into its original string.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./base64ToText-result.png"
        style="width: 100%; padding: 5px;"/>
    </div>