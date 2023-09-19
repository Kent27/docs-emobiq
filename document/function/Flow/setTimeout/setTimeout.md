# setTimeout

## Description

Calls a function or evaluates an expression after a specified number of seconds.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| timeout | The time before a function is executed. | Number | 0 | - | No |
| persistent | To identify whether this should still be executed outside the current active page. | Boolean | false | true, false | No |
| extra | The value to be included to the 'callback' as a system value under 'extra'. | Any | - | - | No |

## Output

N/A

## Callback

### yesCallback

The function to be executed after the timeout.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to display the infoDialog after 1 second.

### Step

1. Call the function "setTimeout"and set the             value for timeout.
   <br>
   timeout: 1000<br>
  
    ![](../../../../document/function/Flow/setTimeout/setTimeout-step-1.png?raw=true)
    
2. Execute the callback coding and call the              function "infoDialog" to display a infoDialog         after 1 seconds.
   <br>
   title: Message<br>
   content: Done<br>
   disableTimer: true<br>
   
    ![](../../../../document/function/Flow/setTimeout/setTimeout-step-2.png?raw=true)
    
### Result

![](../../../../document/function/Flow/setTimeout/setTimeout-result-1.png?raw=true)

It will display the infoDialog after 1 seconds.



## Links