# Device.onBackButton

## Description

Triggers actions when the back button is pressed (only supports Android).

## Input / Parameter

N/A

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

## Callback

### callback

The action performed if this function runs successfully.

| Description | Output Type |
| ------ | ------ |
| The functions to be executed when the back button is triggered.  | Boolean |

## Example

In this example, we will use `Device.onBackButton` for adding actions into back event handler.

```js
Note: This example will only work on android because only android has built-in back button.
```

### Steps

1. Drag a button component to a page in the mobile designer, select the event `press` and drag the `Device.onBackButton` function to the event flow, and drag in Log.write in the callback.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./onBackButton-step-1.png"
        style="width: 50%; padding: 5px;"/>
    </div>

### Result

1. Open the installed app on a device and navigate to another page and then press the button that has `Device.onBackButton` in it's press event.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./onBackButton-result-1.png"
        style="width: 70%; padding: 5px;"/>
    </div>

2. And then press the android's built-in back button at the bottom of the screen, it will navigate to the previous page and call the actions.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./onBackButton-result-2.png"
        style="width: 100%; padding: 5px;"/>
    </div>