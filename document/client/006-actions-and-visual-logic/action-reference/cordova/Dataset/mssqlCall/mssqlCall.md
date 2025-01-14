﻿# mssqlCall 

## Description

Directly access or call a mssql Web Service.

## Input / Parameters

| No | Name | Description | Data Type | Required |
| ------ | ------ | ------ |------ | ------ |
| 1 | connector | Name of connector and created in the Services and Global Components page. | String | Yes  |
| 2 | ent | The Web Service name to be called. | String | Yes |
| 3 | function | The function from the Web Service to be executed. | String | Yes  |
| 4 | data | This contains the main parameter in the function being called. | Object | Yes |
| 5 | filter | Filter details to be used in retrieving the data. | Object | No |
| 6 | orFilter | Filter details to be used in retrieving the data. | Object | No |

## Output

Coming soon.

## Callback

Coming soon.

## Video

Coming soon.

## Example

The user wants to call the mssql Web Service.

### Step

1. Create MSSQL Connector in Services and define the name, url, port,       database, user, password and timeOut.
   <br>Name: mssql<br>
   url: mkals4utt4.database.windows.net
   port: 1433<br>
   database: emobiq_demo_1<br>
   user: sqladmin<br>
   password: ********<br>
   timeOut: 5000
 
   ![](./mssqlCall-step-1.png)
  
2. Create MSSQL Table in Services and  define the Name, connector,          listKey and serviceName timeOut.
   <br>Name: tbl_1<br>
   mssql: mssql<br>
   listKey: data<br>
   serviceName: user_package<br>
   
   ![](./mssqlCall-step-2.png)
   
3. Fill in the field caption for MssqlDataset Fields and generate           datalist.
   <br>
   Field Caption: 1,2,3,4,5,6<br> 
   
   ![](./mssqlCall-step-3.png)
   
   ![](./mssqlCall-step-4.png)<br>
 
   
4. Call the function "mssqlCall"and define the connector, ent,              function and set the function"toObject"to data.
   <br>connector: mssql<br>
   ent: user_package<br>
   function: insert<br>
   data: toObject<br>
    
   ![](./mssqlCall-step-5.png)
   
5. Define the column and value for object. ( Please refer to the images     below, we have our own database:emobiq_demo_1 and inside this database    we have 6 column which are id(not need to create due to the id no will    auto increment), icnum, name, handphone, address, package.)
   <br>
   icnum: 9<br>
   name: 9<br>
   handphone: 9<br>
   address: 9<br>
   package: 9 (auto display 1)<br>
   
   ![](./mssqlCall-step-6.png)
   
   ![](./mssqlCall-step-7.png) 

6. Add a console for display the response from console.<br>
   
   ![](./mssqlCall-step-8.png)
   
### Result
  
 ![](./mssqlCall-result-1.png)
  
 ![](./mssqlCall-result-2.png)


## Links

Coming soon.