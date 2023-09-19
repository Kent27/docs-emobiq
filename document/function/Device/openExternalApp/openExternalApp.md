# openExternalApp

## Description

Opens an external mobile app and passes the data specified to that app.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| path | The path of the mobile app. | String/Text | - | - | Yes |
| data | The data to be passed to the mobile app. | String/Text | - | - | Yes |

## Output

N/A

Note: The app will be updated to show the data to be passed in the external mobile app.

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user want send a Whatsapp message from current app to Whatsapp.

### Step

1. Call the openExternalApp function in a button event.

    ![](../../../../document/function/Device/openExternalApp/openExternalApp-step-1.png?raw=true)
    
### Result

The Whatsapp will be opened, select who to send the message "1111" will be sent.
![](../../../../document/function/Device/openExternalApp/openExternalApp-result-1.png?raw=true)



## Links