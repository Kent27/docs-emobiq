# Validation.isList

## Description

Checks whether the value input is a list.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| value | The value to be checked. | Any | - | - | Yes |

## Output

N/A

## Example

In this example, we will check whether a list is valid and print the result in the console.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Validation.isList` inside the `Log.write` function.
3. Enter the value for the list to be validated. In this example, we will enter the value "not a list".

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./isList-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The console will print `false` since it is not a valid List.
