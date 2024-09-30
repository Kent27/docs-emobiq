# Conversion.textToBase64

## Description

Converts text into a Base64 encoded string.

## Input / Parameter

| Name  | Description                                             | Input Type | Default | Options | Required |
| ----- | -------------------------------------------------------| ---------- | ------- | ------- | -------- |
| value | The text to be converted to Base64.  | Text/List  | -       | -       | Yes      |

## Output

| Description                                   | Output Type |
| --------------------------------------------- | ----------- |
| Returns the base64.            | Text      |

### Steps

1. Drag a `Button` component into the service page that will trigger the Base64 conversion action.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./textToBase64-step-1.png"
        style="width: 50%; padding: 5px;"/>
    </div>

2. Select the event `press` for the button and drag the `Conversion.textToBase64` function to the event flow. Fill in the parameter with the text or list to be converted.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./textToBase64-step-2.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. Upon pressing the button, the text or list of texts will be converted to a Base64 encoded string.