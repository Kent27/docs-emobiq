# Conversion.base64ToText

## Description

Converts Base64 encoded text strings back into their original text format.

## Input / Parameter

| Name  | Description                                             | Input Type | Default | Options | Required |
| ----- | -------------------------------------------------------| ---------- | ------- | ------- | -------- |
| value | The Base64 encoded text strings to be converted. | Text/List  | -       | -       | Yes      |

## Output

| Description                                   | Output Type |
| --------------------------------------------- | ----------- |
| Returns the original text format.            | Object      |

### Steps

1. Drag a `Button` component into the service page that will trigger the Base64 decoding action.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./base64ToText-step-1.png"
        style="width: 50%; padding: 5px;"/>
    </div>

2. Select the event `press` for the button and drag the `Conversion.base64ToText` function to the event flow. Fill in the parameter with the Base64 encoded text or list to be converted.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./base64ToText-step-2.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. Upon pressing the button, the Base64 encoded text or list will be decoded back into its original string(s).