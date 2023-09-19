# navCall

## Description

Creates a connection with a navConnector.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| connector | The name of the navConnector created in Services to connect to. | String/Text | - | - | Yes |
| type | The type of connection. | String/Text | - | - | No |
| ent? |  | String/Text | - | - | Yes |
| function | The function from the web service to be executed. | String/Text | - | - | Yes |
| subfunction | The subfunction from the web service to be executed. | String/Text | - | - | No |
| data | The data containing the main parameters in the function being called. | Object | - | - | Yes |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |
| batch? |  | String/Text | - | - | No |

## Output

N/A

## Callback?

### callback

The function to be executed if the connection to navConnector is successful.

### errCallback

The function to be executed if the connection to navConnector is not successful.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to call the navCall Web Service.

### Step

1. Create NAV Connector in Services.<br>
   Name: nav<br>
   url: http://203.116.137.100:8047/DynamicsNAV90<br> 
   company: CRONUS Australia Pty. Ltd.
   user: chh\mobuser<br>
   password: ********<br>
   timeOut: 30000<br>
   
   ![](../../../../document/function/Dataset/navCall/navCall-step-1.png?raw=true)
   
   
2. Call the function "navCall".
   <br>
   
   ![](../../../../document/function/Dataset/navCall/navCall-step-2.png?raw=true)
   
  
3. Add a console after callback function for       display response from console.   
   
   ![](../../../../document/function/Dataset/navCall/navCall-step-3.png?raw=true)
 
### Result
   
   ![](../../../../document/function/Dataset/navCall/navCall-result-1.png?raw=true)



## Links