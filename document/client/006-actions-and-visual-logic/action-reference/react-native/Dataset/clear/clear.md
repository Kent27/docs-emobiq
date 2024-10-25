# Dataset.clear

## Description

Clears all rows of data from a specified dataset.

## Input / Parameter

| Name    | Description                                             | Input Type | Default | Options | Required |
| ------- | -------------------------------------------------------| ---------- | ------- | ------- | -------- |
| dataset | The name of the dataset that will be cleared.         | Text/List  | -       | -       | Yes      |
| extra   | The stored value that is passed to all the callbacks.  | Any        | -       | -       | No       |

## Output

| Description                                  | Output Type |
| --------------------------------------------- | ----------- |
| Returns the formatted information.            | Object      |

## Callback

### callback

The action performed if this function runs successfully.

| Description                                  | Output Type |
| --------------------------------------------- | ----------- |
| Returns a confirmation of the clearing action.| Object      |

### errorCallback

The action performed if this function does not run successfully.

| Description                                  | Output Type |
| --------------------------------------------- | ----------- |
| Returns an error message.                    | Text       |

## Example

In this example, we will clear all rows of data from a specified datasets.

### Steps

1. Drag a `Button` component into the service page that will trigger the clearing action.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clear-step-1.png"
        style="width: 50%; padding: 5px;"/>
    </div>

2. Select the event `press` for the button and drag the `Dataset.clear` function to the event flow. Fill in the parameters with the list of the datasets you want to clear.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clear-step-2.png"
        style="width: 70%; padding: 5px;"/>
    </div>

     <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./clear-step-3.png"
        style="width: 70%; padding: 5px;"/>
    </div>

### Result

1. Upon pressing the button, all rows of data from the specified dataset will be cleared.