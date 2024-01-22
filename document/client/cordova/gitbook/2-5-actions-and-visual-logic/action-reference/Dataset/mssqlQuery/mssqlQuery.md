# mssqlQuery 

## Description

Query languages are used to make queries in a database, and Microsoft Structured Query Language (SQL) is used to query, insert, update and modify data.

## Input / Parameters

| No | Name | Description | Data Type | Required |
| ------ | ------ | ------ |------ | ------ |
| 1 | connector | Name of connector and created in the Services and Global Components page. | String | Yes  |
| 2 | query | A query is a request for data or information from a database table or combination of tables. | String | Yes |

## Output

## Callback

## Video

## Example

The user wants to call the mssqlQuery 
Web Service.

### Step

1. To create MSSQL Connector in Services and          define the  name, url, port, database,             user, password and timeOut.
   <br>Name: mssql<br>
   url: mkals4utt4.database.windows.net
   port: 1433<br>
   database: emobiq_demo_1<br>
   user: sqladmin<br>
   password: ********<br>
   timeOut: 5000
 
   ![](./mssqlQuery-step-1.png)
  
2. Call the function "mssqlQuery"and define the       connector and query.
   <br>connector: mssql<br>
   query: select * from user_package<br>
    
   ![](./mssqlQuery-step-2.png)
   
3. Add a console for display the response from        console.<br>

   ![](./mssqlQuery-step-3.png)

### Result

![](./mssqlQuery-result-1.png)

  
## Links