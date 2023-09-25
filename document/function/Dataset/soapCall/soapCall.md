# soapCall  

## Description

Directly access or call a SOAP Web Service.

## Input / Parameters

| No | Name | Description | Data Type | Required |
| ------ | ------ | ------ |------ | ------ |
| 1 | connector | Name of connector and created in the Services and Global Components page. | String | Yes  |
| 2 | function | The function from the Web Service to be executed. | String | Yes  |
| 3 | data | This contains the main parameter in the function being called. | Object | No |

## Output

Coming soon.

## Callback

Coming soon.

## Video

Coming soon.


## Example

The user wants to call the SOAP Web Service.


### Step

1. To create SOAP Connector in Services and           define the name, url and timeOut.
   <br>Name: soap<br>
   url: http://203.116.137.100:51059/Training/Main.asmx ( Please refer to the picture below, there is a example of main web service.We have take one of the operation which is login as an example to apply for this function.)<br>
   timeOut: 3000
   
   ![](../../../../document/function/Dataset/soapCall/soapCall-step-1.png?raw=true)
   
   ![](../../../../document/function/Dataset/soapCall/soapCall-step-2.png?raw=true)
  
2. Call the function "soapCall"and define the         connector, function and set the                    function"toObject" to data.
   <br>connector: soap<br>
   function: login<br>
   data: toObject<br>
   
   ![](../../../../document/function/Dataset/soapCall/soapCall-step-3.png?raw=true)
   
3. Define the toObject(parameter)which are            username and password and the                      component value.    
   username: componentValue (for defined the name in     textbox.)<br>
   component: txtUsername<br>
   
   password: componentValue ( for defined the password in textbox.)<br>
   component: txtPassword<br>
 
    ![](../../../../document/function/Dataset/soapCall/soapCall-step-4.png?raw=true)
    
    ![](../../../../document/function/Dataset/soapCall/soapCall-step-5.png?raw=true)
    
    ![](../../../../document/function/Dataset/soapCall/soapCall-step-6.png?raw=true)
   
4. Add a console for display the response from        console.<br>
 
    ![](../../../../document/function/Dataset/soapCall/soapCall-step-7.png?raw=true)
   
### Result

![](../../../../document/function/Dataset/soapCall/soapCall-result-1.png?raw=true)  
  

## Notes

- N/A