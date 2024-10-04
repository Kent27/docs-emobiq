# whileLoop

## Description

Loop runs, and it continues to repeat as long as the condition remains true, it evaluates the condition first before looping.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| condition | The condition to evaluates first before loop | boolean | - | - | Yes |

## Output

N/A

## Callback

### yesCallback

This will be triggered for every loop that happens while the condition remains true.

## Example

In this example, we will do console logging by using `console` function in `whileLoop` callback

### Code Equivalent

```
let n = 0;
while (n < 5) {
  n++;
  console.log("while loop"+n);
}
```

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `setVar` function to the event flow, add the value `n` on `var` param and add the value `0` on `value` param.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./whileLoop-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

2. Drag the function `whileLoop` to the eventflow, on it's `condition` param change the param type to function/subflow then add function `less` inside the subflow, for the `value1` param change the param type to function/subflow then add function `getVar` inside the subflow, for the `var` param add value `n`.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./whileLoop-step-2.png"
        style="width: 100%; padding: 5px;"/>
    </div>

3. Drag the function `setVar` inside function `whileLoop` yes callback, add value `n` on param `var` and change the param type to subflow/function on param `value`. Inside param `value` subflow add `add` function then on it's `value1` change the param type to subflow/function, add `getVar` function in it, then put `n` on it's `var` param value.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./whileLoop-step-3.png"
        style="width: 100%; padding: 5px;"/>
    </div>

4. Drag the function `console` inside function `whileLoop` yes callback, change the param type to subflow/function on param `value`. Inside param `value` subflow add `plus` function then on it's `value1` param add `while loop` value, as for `value2` param change the param type to subflow/function, add `getVar` function in it, then put `n` on it's `var` param value.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./whileLoop-step-4.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. Now click the button in preview, it will show the list of `while loop` with the current loop number on the console.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./whileLoop-result-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

## Links

### Related Information

See also:

- Functions
    -  [plus](/document/client/006-actions-and-visual-logic/action-reference/cordova/Math/plus/plus.md)