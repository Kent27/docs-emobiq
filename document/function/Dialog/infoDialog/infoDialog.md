# infoDialog

## Description

Displays a dialog box (modal) that shows some message set by the user.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| title | The title of the dialog box. | String/Text | - | - | Yes |
| content | The message to be shown in the dialog box. | String/Text | - | - | Yes |
| disableTimer | To disable the timer or not. | Boolean | false | true, false | No |
| timeOut | The duration that the modal appears on the screen for. (1 second = 1000) | Number | - | - | No |
| okCaption | The label for the 'OK' button. | String/Text | - | - | No |
   
## Output

N/A

Note: A modal will pop up which displays the parameters specified by the user.

## Callback

### okCallback

The function to be executed when user clicks on the button in the modal.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to display an information dialog.

### Step

1. Call the function "infoDialog" and set the            value.
   <br>
   title: Message<br/>
   content: Updated Successful.<br/>
   timeOut: 30000<br/>
   
   ![](../../../../document/function/Dialog/infoDialog/infoDialog-step-1.png?raw=true)

### Result
The following info dialog will be displayed and shows the information. It will be time out in 30 seconds. <br>
   ![](../../../../document/function/Dialog/infoDialog/infoDialog-result-1.png?raw=true)
   
   


## Links