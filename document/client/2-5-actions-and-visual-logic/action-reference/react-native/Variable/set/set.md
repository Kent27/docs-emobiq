# Variable.set

## Description

Creates a global variable with a value associated to it.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| name | The name of the variable to create. | String/Text | - | - | Yes |
| value | The value associated to the variable. | String/Text | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| success | Boolean value to denote whether the function was executed successfully. | Text |
| message | The message to print. | Text |
| data | Any additional message or data to print. | Text |

## Example

In this example, we will set the value of a global variable and check whether the variable has been set successfully in the console.

### Steps

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Variable.set` inside the `value` parameter of the `Log.write` function. (*Note: The `Log.write` function is used here for ease of demostrating the output.)
3. Create a variable called `version` with the value `1.0.0`

![](./set-step-1.png)

4. This will create a global variable called "version" containing the value "1.0.0" that can be accessed by other components or on other pages of your app.

### Result

1. The value of the global variable `version` can be accessed by using the function `Variable.get`. 
2. Using the above flow will display the value `1.0.0` in the browser console.

![](./set-result-1.png) 

## Links

### Related Information

See also:

-  [Variable.get](/document/client/gitbook/2-5-actions-and-visual-logic/action-reference/react-native/Variable/get/get.md)