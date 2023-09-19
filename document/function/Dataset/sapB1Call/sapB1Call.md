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
   <br>Name: sapb1<br>
   url: http://203.116.137.100:51059/DemoApp/Sample.asmx<br> ( Please refer to the picture below, there is a example of main web service.We have take one of the operation which is LoginDemo as an example to apply for this function.)<br>
   timeOut: 30000
   
   ![](../../../../document/function/Dataset/sapB1Call/sapB1Call-step-1.png?raw=true)
   
   ![](../../../../document/function/Dataset/sapB1Call/sapB1Call-step-2.png?raw=true)
   
2. Call the function "sapB1Call" and define           the connector & function, set the                    function "toObject"to data.
   <br>
   connector: sapb1<br>
   function: LoginDemo<br>
   data: toObject<br>
   
   ![](../../../../document/function/Dataset/sapB1Call/sapB1Call-step-3.png?raw=true)
   
3. Define toObject.
   <br>
   CompanyUserName: manager<br>
   CompanyPassword: 123456<br>

   ![](../../../../document/function/Dataset/sapB1Call/sapB1Call-step-4.png?raw=true)
  
4. Add a console after callback function for       display response from console.   
   
   ![](../../../../document/function/Dataset/sapB1Call/sapB1Call-step-5.png?raw=true)
 
### Result
   
![](../../../../document/function/Dataset/sapB1Call/sapB1Call-result-1.png?raw=true)



## Links