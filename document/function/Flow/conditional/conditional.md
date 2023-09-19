# conditional

## Description

Checks whether the condition passed is met and executes the callback functions accordingly.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| condition | The condition to be checked against. | String/Text | - | - | Yes |
| yesValue | The output value if condition is 'true'. | Any | - | - | No |
| noValue | The output value if condition is 'false. | Any | - | - | No |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the 'yesValue' or 'noValue'. | Any |

## Callback

### yesCallback

The function to be executed when the condition passed is 'true'.

### noCallback

The function to be executed when the condition passed is 'false'.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example

<<<<<<< HEAD
=======
The user wants to prove that the value `13` is greater than the value `1` and see the result in the console.
>>>>>>> 69d54562a741115d9ec269e947a0c097684e99ce

The user wants to prove that the value 13 is greater than the value 1.</br>

### Step

<<<<<<< HEAD
1. Call the function "greater" and set the               value.<br>
   value1: 13<br/>
   value2:  1<br/>
  
   ![](../../../../document/function/Flow/conditional/conditional-step-1.png?raw=true)
   
2. Add a console and set the value if the                condition is met then the program will execute    a     code from "yesCallback".<br>
   value : greater<br/>
=======
| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](../conditional/conditional-step-1.png?raw=true) ![](../conditional/conditional-step-2.png?raw=true) | Drag a button to a page in the mobile designer. Select the event `click` for the button and drag the `conditional` function to the event flow. Select the `function` parameter input type for the `condition` parameter. |
| 2. | ![](../conditional/conditional-step-3.png?raw=true) | Drag the function `greater` to the subflow. |
| 3. | ![](../conditional/conditional-step-4.png?raw=true) | Fill in the inputs of the `greater` function. |
| 4. | ![](../conditional/conditional-step-5.png?raw=true) | Drag the function `console` to the `yesCallback` and `noCallback` nodes of the `conditional` function. |
| 5. | ![](../conditional/conditional-step-6.png?raw=true) ![](../conditional/conditional-step-7.png?raw=true) | The `console` function in `yesCallback` should return 'greater' while the `console` function in `noCallback` should return 'not greater'. |
>>>>>>> 69d54562a741115d9ec269e947a0c097684e99ce

   ![](../../../../document/function/Flow/conditional/conditional-step-2.png?raw=true)
   
3. Add a console and set the value if the                condition is not met so the program will              execute a code from "noCallback". <br>
   value : not greater<br/>
   
   ![](../../../../document/function/Flow/conditional/conditional-step-3.png?raw=true)

### Result

<<<<<<< HEAD
"greater" 
=======
When the button is pressed, the console will print 'greater'.
>>>>>>> 69d54562a741115d9ec269e947a0c097684e99ce



## Links