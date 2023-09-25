# deleteData 

## Description

Delete a record from a staging database.


## Input / Parameters

| No | Name | Description | Data Type | Required |
| ------ | ------ | ------ |------ | ------ |
| 1 | dataset | Name of the dataset in staging table which will be deleted. | String | Yes  |
| 2 | _id | Value from the staging database and used for identify which record will be updated. | Integer | Yes  |

## Output

## Callback

## Video

## Example

The user wants to delete the data from staging table.

### Step

1. Create a table with a table name and fields in staging table and             create a dataset in Services. (We assumed that the table ,               fields and dataset have been created.)
   <br>
   table name: customer<br>
   Fields name: tel, name and add<br>
   Dataset: customer_1<br>
   Set value: tel:34345678, name: 111, add:abc<br>
        
   ![](../../../../document/function/Dataset/deleteData/deleteData-step-1.png?raw=true)
        
2. Call the function "deleteData", define the dataset and id. 
   <br>
   dataset: customer_1<br>
   _id: 10<br>
   
   ![](../../../../document/function/Dataset/deleteData/deleteData-step-2.png?raw=true)
 
3. Call the function "loadData" and set the dataset.
   <br>
   dataset: customer_1<br>
   
   ![](../../../../document/function/Dataset/deleteData/deleteData-step-3.png?raw=true)
   
4. Add a console after callback for display the response from               console.
 
   ![](../../../../document/function/Dataset/deleteData/deleteData-step-4.png?raw=true)
   

### Result

 ![](../../../../document/function/Dataset/deleteData/deleteData-result-1.png?raw=true)
 
 ![](../../../../document/function/Dataset/deleteData/deleteData-result-2.png?raw=true)<br>
 ( The result display in editor.)
 
 ![](../../../../document/function/Dataset/deleteData/deleteData-result-3.png?raw=true)
( The row for tel:34345678, name: 111, add:abc have been remove successfully.)

## Links