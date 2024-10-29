# Device.chooseDateTime

## Description

Customize a datetime picker with different formats.

## Input / Parameter

| Name         | Description             | Input Type | Default | Options | Required |
| ------------ | ----------------------- | ---------- | ------  | ------  | -------- |
| mode         | The mode of the picker. | Text       | -       | -       | No       |
| selectedDate | The selected date.      | Text       | -       | -       | No       |
| minimumDate  | The minimum date.       | Text       | -       | -       | No       |
| maximumDate  | The maximum date.       | Text       | -       | -       | No       |

## Output

| Description                        | Output Type |
| ---------------------------------- | ----------- |
| Returns the formatted information. | Text        |

## Callback

### callback

The function to be executed when the user finish picked the date.

### errorCallback

The function to be executed when the user failed to picked the date.

## Example

In this example, we will create an example button and when user click, we will show date picker based on setup parameters.

### Steps

1. Drag a button component to a page in the mobile designer. 
   
   <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./chooseDateTime-step-1.png"
        style="width: 40%; padding: 5px;"/>
    </div>
   
2. Select the event `press` and drag the function `Device.chooseDateTime` to the event flow and fill the parameters.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./chooseDateTime-step-2.png"
        style="width: 40%; padding: 5px;"/>
    </div>

3. In this example, we are using the `Log.write` function as the yes callback and take input as the log.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./chooseDateTime-step-3.png"
        style="width: 80%; padding: 5px;"/>
    </div>

### Result

1. On the app we can open the date time picker based on setup.

    Android:
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./chooseDateTime-result-android.png"
        style="width: 80%; padding: 5px;"/>
    </div>

    IOS:
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./chooseDateTime-result-ios.png"
        style="width: 80%; padding: 5px;"/>
    </div>

    Platform Preview (The design will be different on native app but the functions will remain the same):
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./chooseDateTime-result-web.png"
        style="width: 80%; padding: 5px;"/>
    </div>