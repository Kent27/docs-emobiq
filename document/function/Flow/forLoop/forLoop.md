# forLoop

## Description
 
Loops through the parameter over a range, from the start to the end of the range with an increment of 1 step after every loop to execute a statement until a particular condition is satisfied.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| start | The first value in the range to be looped over. | Number | - | - | Yes |
| end | The last value in the range to be looped over. | Number | - | - | Yes |

## Output

N/A

## Callback

### yesCallback

This will be triggered for every loop that happens within the range.

| Description | Output Type |
| ------ | ------ |
| The current active value within the range. | Number |

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to set the loop condition to run which starting from 1 to 12.

### Step

1. Call the function "forLoop"and defines the            condition for the loop to run.
   <br>
   start: 1<br>
   end : 12
   
   ![](../../../../document/function/Flow/forLoop/forLoop-step-1.png?raw=true)
    
2. Add a console and display the response from           console.
   <br>
   
    ![](../../../../document/function/Flow/forLoop/forLoop-step-2.png?raw=true)
    
### Result

![](../../../../document/function/Flow/forLoop/forLoop-result-1.png?raw=true)



## Links