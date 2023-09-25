# axCall 

## Description

Axcall is the general purpose AX.25, NET/ROM and Rose connection program. 

## Input / Parameters

| No | Name | Description | Data Type | Required |
| ------ | ------ | ------ |------ | ------ |
| 1 | connector | Name of connector and created in the Services and Global Components page. | String | Yes  |
| 2 | ent | The Web Service name to be called. | String | Yes  |
| 3 | data | This contains the  parameter in the function being called. | Object | Yes |

## Output

## Callback

## Video

## Example

The user wants to call the axCall Web Service.

### Step

1. Create AX Connector in Services and define the name, url,        user, password and timeOut.
   <br>Name: axConnector<br>
   url: http://203.116.137.100:8109/MicrosoftDynamicsAXAif60/ABJCustSelfOrderingServices/xppservice.svc?wsdl<br>( Please refer to the picture below, there is a example of main web service.We have take one of the operation as an example to apply for this function.)<br>
   user: contoso\administrator<br>
   password: ********<br>
   timeOut: 30000
   
   ![](../../../../document/function/Dataset/axCall/axCall-step-1.png?raw=true)
   
2. Call the function "axCall" and define the connector & ent, set    the function "toObject"to data.
   <br>
   connector: axConnector<br>
   ent: validateCustLogin<br>
   data: toObject<br>
   
   ![](../../../../document/function/Dataset/axCall/axCall-step-2.png?raw=true)
   
3. Define toObject.
   <br>
   _companyId: USMF<br>
   _accountNum: SG-001<br>
   _password: 1234<br>
    
   ![](../../../../document/function/Dataset/axCall/axCall-step-3.png?raw=true)
   
4. Add a console after callback function for display response       from console.   
   
   ![](../../../../document/function/Dataset/axCall/axCall-step-4.png?raw=true)
 
### Result

![](../../../../document/function/Dataset/axCall/axCall-result-1.png?raw=true)


## Links