# sapB1Call

## Description

This is a business management software (ERP) designed for small and medium-sized enterprises. As an ERP solution, it aims to automate key business functions in financials, operations, and human resources.

This function allows users to call the sapB1Call web service.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| connector | The name of the SAP B1 connector created in Services to connect to. | String/Text | - | - | Yes |
| function | The function from the web service to be executed. | String/Text | - | - | Yes |
| data | The data containing the main parameters in the function being called. | Object | - | - | Yes |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

N/A

## Callback?

### callback

The function to be executed if the connection to SAP B1 connector is successful.

### errCallback

The function to be executed if the connection to SAP B1 connector is not successful.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to call the sapB1Call Web Service.

### Step

1. Create SAP B1 Connector in Services and         define the name, url and timeOut.

   |  |  | 
   | ---- | ---- | 
   | Name | sapb1 |
   | Url | http://203.116.137.100:51059/DemoApp/Sample.asmx | 
   | Timeout | 30000 | 
   
   ![](./sapB1Call-step-1.png?raw=true)
   
   
2. Call the function "sapB1Call" and define           the connector & function, set the                    function "toObject"to data.
   
   |  |  | 
   | ---- | ---- | 
   | connector | sapb1 | 
   | function | LoginDemo | 
   | data | toObject | 

   
   ![](./sapB1Call-step-2.png?raw=true)
   
3. Define toObject.

   |  |  | 
   | ---- | ---- | 
   | CompanyUserName | manager | 
   | CompanyPassword | 123456 | 

   ![](./sapB1Call-step-3.png?raw=true)
  
1. Add a console after callback function for       display response from console.   
   
   ![](./sapB1Call-step-4.png?raw=true)
 
### Result
   
![](./sapB1Call-result-1.png?raw=true)



## Links