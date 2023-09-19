# confirmDialog

## Description

Displays a dialog box (modal) that asks for confirmation from the user.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| title | The title of the dialog box. | String/Text | - | - | Yes |
| content | The message to be shown in the dialog box. | String/Text | - | - | Yes |
| okCaption | The label for the 'OK' button. | String/Text | - | - | No |
| cancelCaption | The label for the 'Cancel' button. | String/Text | - | - | No |

## Output

N/A

Note: A modal will pop up which displays the parameters specified by the user.

## Callback

### okCallback

Functions to be executed when the user clicks the 'OK' button.

### cancelCallback

Functions to be executed when the user clicks the 'Cancel' button.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to display a dialog box for ask the comfirmation from the user.

### Step

1. Call the function "confirmDialog" and set the    value for parameters.
   <br>
   title: Confirm<br/>
   content: Are you sure you want to delete?<br/>
   okCaption: Delete<br/>
   cancelCaption: Exit<br/>
   
   ![](../../../../document/function/Dialog/confirmDialog/confirmDialog-step-1.png?raw=true)
   
   ![](../../../../document/function/Dialog/confirmDialog/confirmDialog-step-2.png?raw=true)
   
2. Set a function in okCallback.
   <br>
   function:setVar<br/>
   var:Message<br/>
   value: Delete<br/>
   
   ![](../../../../document/function/Dialog/confirmDialog/confirmDialog-step-3.png?raw=true)

### Result

![](../../../../document/function/Dialog/confirmDialog/confirmDialog-result-1.png?raw=true)



## Links