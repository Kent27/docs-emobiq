# Text.length

## Description

Counts the total number of characters in the text.

## Input / Parameter

| Name   | Description             | Input Type | Default | Options | Required |
| ------ | ----------------------- | ---------- | ------- | ------- | -------- |
| text   | The text to be counted. | Text       | -       | -       | Yes      | 

## Output

| Description                | Output Type  |
| -------------------------- | ------------ |
| Returns the total length.  | Number       |

## Example

In this example, we will count the total of a string.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button.
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./length-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>
   
2. Add `Log.write` function and add a subflow on it's value.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./length-step-2.png"
        style="width: 100%; padding: 5px;"/>
    </div>

3. Then put `Text.length` inside it and fill the text "Hello World!"

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./length-step-3.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The console will return the total length of text.
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./length-result.png"
        style="width: 100%; padding: 5px;"/>
    </div>