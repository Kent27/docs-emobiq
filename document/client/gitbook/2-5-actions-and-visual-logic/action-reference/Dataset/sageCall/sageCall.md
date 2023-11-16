# sageCall

## Description

Is a function that are needed when user want to use sage table.

## Input / Parameters

| No | Name | Description | Data Type | Required |
| ------ | ------ | ------ |------ | ------ |
| 1 | connector | Name of connector and created in the Services and Global Components page. | String | Yes  |
| 2 | ent | Name of Sage table | String | Yes  |
| 3 | function | The function from the Web Service to be executed. | String | Yes  |
| 4 | data | This contains the main parameter in the function being called. | Object | No |
| 5 | extra |  |  | No |

## Output

## Callback

## Video

## Example

The user wants to use Sage table.

### Step

1. Create SAGE Connector in Services and         define the name, url and timeOut.
   <br>Name: conn
   <br>url: http://sage300demo.sageasiapac.com 
   <br>basepath: /Sage300WebApi
   <br>apiVersion: 1.0
   <br>tenant: -
   <br>company: SAMLTD
   <br>user: DEMO
   <br>password: ****
   <br>timeOut: 30000
   
   ![](./sageCall-step-1.png)
   
   
2. Make sure Sage table exist inside the services.

	![](./sageCall-step-2.png)

   
3. Call the function "sageCall".

   ![](./sageCall-step-3.png)
  
4. Add a console after callback function for       display response from console.   
   
   ![](./sageCall-step-4.png)
 
### Result
   
![](./sageCall-result-1.png)

## Links

- N/A