# Conversion.binaryToBase64

## Description

Converts binary data into a Base64 encoded string.

## Input / Parameter

| Name  | Description                                                             | Input Type | Default | Options | Required |
| ----- | ----------------------------------------------------------------------- | ---------- | ------- | ------- | -------- |
| value | The binary data to be converted to Base64.                              | Byte_Array | -       | -       | Yes      |
| extra | Any additional value that is passed to all the callbacks.               | Any        | -       | -       | No       |

## Output

| Description                                 | Output Type |
| ------------------------------------------- | ----------- |
| Returns the formatted information.          | Text        |

## Callback

### callback

The action performed if this function runs successfully.

| Description                                     | Output Type |
| ----------------------------------------------- | ----------- |
| Returns the Base64 encoded data.                | Object      |

### errorCallback

The action performed if this function does not run successfully.

| Description                                 | Output Type |
| ------------------------------------------- | ----------- |
| Returns an error message.                   | Text        |

## Example

In this example, we will convert binary data from a file into Base64 string when a button is pressed.

### Steps

1. Drag a `Button` component into the service page that will trigger the Base64 conversion action.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./binaryToBase64-step-1.png"
        style="width: 50%; padding: 5px;"/>
    </div>

2. Select the event `press` for the button and drag the `File.read` function to the event flow. Fill in the parameters: fileName, folder, and dataType use the Byte_Array.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./binaryToBase64-step-2.png"
        style="width: 60%; padding: 5px;"/>
    </div>

3. On the success callback, drag the `Conversion.binaryToBase64` and Fill in value as input result from `File.read` function.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./binaryToBase64-step-3.png"
        style="width: 60%; padding: 5px;"/>
    </div>

4. Put `Log.write` function below the success callback of `Conversion.binaryToBase64`, to get the result.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./binaryToBase64-step-4.png"
        style="width: 60%; padding: 5px;"/>
    </div>

### Result

1. Upon pressing the button, the binary data will be converted to a Base64 encoded string.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./binaryToBase64-result.png"
        style="width: 100%; padding: 5px;"/>
    </div>