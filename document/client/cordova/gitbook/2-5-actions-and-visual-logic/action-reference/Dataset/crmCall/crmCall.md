# crmCall

## Description

Is a business management software (ERP) designed for small and medium-sized enterprises. As an ERP solution, it aims to automate key business functions in financials, operations, and human resources.

## Input / Parameters

| No | Name | Description | Data Type | Required |
| ------ | ------ | ------ |------ | ------ |
| 1 | connector | Name of connector and created in the Services and Global Components page. | String | Yes  |
| 2 | function | The function from the Web Service to be executed. | String | Yes  |
| 3 | data | This contains the main parameter in the function being called. | Object | Yes |
| 4 | extra |  |  |  |

## Output

## Callback

## Video

## Example

The user wants to call the sapB1Call Web Service.

### Step

1. Create SAP B1 Connector in Services and         define the name, url and timeOut.
   <br>Name: sapb1<br>
   url: http://203.116.137.100:51059/DemoApp/Sample.asmx<br> ( Please refer to the picture below, there is a example of main web service.We have take one of the operation which is LoginDemo as an example to apply for this function.)<br>
   timeOut: 30000
   
   ![](./sapB1Call-step-1.png)
   
   ![](./sapB1Call-step-2.png)
   
2. Call the function "sapB1Call" and define           the connector & function, set the                    function "toObject"to data.
   <br>
   connector: sapb1<br>
   function: LoginDemo<br>
   data: toObject<br>
   
   ![](./sapB1Call-step-3.png)
   
3. Define toObject.
   <br>
   CompanyUserName: manager<br>
   CompanyPassword: 123456<br>

   ![](./sapB1Call-step-4.png)
  
4. Add a console after callback function for       display response from console.   
   
   ![](./sapB1Call-step-5.png)
 
### Result
   
![](./sapB1Call-result-1.png)

## Links## Notes

- N/A