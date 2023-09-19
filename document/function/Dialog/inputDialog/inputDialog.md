# inputDialog

## Description

Displays a dialog box (modal) that requires the user to enter some input.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| title | The title of the dialog box. | String/Text | - | - | Yes |
| type | The type of input to enter in the dialog box. | String/Text | - | - | Yes |
| value | Default value to be displayed in the input field of the dialog box. | Integer | - | - | No |
   
## Output

N/A

Note: A modal will pop up which displays the parameters specified by the user.

## Callback

### okCallback

The function to be executed when user clicks on the 'OK' button.

### cancelCallback

The function to be executed when user clicks on the 'Cancel' button.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to display an input dialog to let the user to key in the quantity.

### Step

1. Call the function "inputDialog" and set the           value.
   <br>
   title: Please Key In the Quantity<br/>
   type: quantity<br/>
  
   ![](../../../../document/function/Dialog/inputDialog/inputDialog-step-1.png?raw=true)
   
2. Set the function "setVar" in okCallback.
   <br>
   var: vCorrectValue <br>
   value: input
   
   ![](../../../../document/function/Dialog/inputDialog/inputDialog-step-2.png?raw=true)

### Result

![](../../../../document/function/Dialog/inputDialog/inputDialog-result-1.png?raw=true)



## Links