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


The user wants to prove that the value 13 is greater than the value 1.</br>

### Step

1. Call the function "greater" and set the               value.<br>
   value1: 13<br/>
   value2:  1<br/>
  
   ![](../../../../document/function/Flow/conditional/conditional-step-1.png?raw=true)
   
2. Add a console and set the value if the                condition is met then the program will execute    a     code from "yesCallback".<br>
   value : greater<br/>

   ![](../../../../document/function/Flow/conditional/conditional-step-2.png?raw=true)
   
3. Add a console and set the value if the                condition is not met so the program will              execute a code from "noCallback". <br>
   value : not greater<br/>
   
   ![](../../../../document/function/Flow/conditional/conditional-step-3.png?raw=true)

### Result

"greater" 



## Links