# insertData

## Description

Insert or add value in a staging database.

## Input / Parameters

| No | Name | Description | Data Type | Required |
| ------ | ------ | ------ |------ | ------ |
| 1 | dataset | Name of the dataset in stagging table where the record will be inserted. | String | Yes  |
| 2 | param | Object name | Object | Yes |

## Output

## Callback

## Video

## Example

The user wants to insert the data into staging table.

### Step

1. Create a table with a table name and field in      staging table. 
   <br>
   table name: customer<br>
   Fields name: tel, name and add
                
   ![](../../../../document/function/Dataset/insertData/insertData-step-1.png?raw=true)
   
   ![](../../../../document/function/Dataset/insertData/insertData-step-2.png?raw=true)
   
2. Create a dataset is  in Services.
   <br>
   dataset: customer_1<br>
   
   ![](../../../../document/function/Dataset/insertData/insertData-step-3.png?raw=true)

3. Call the function "insertData", define the         dataset and set function "toObject"to              param.
   <br>
   dataset: customer_1<br>
   param: toObject<br/>
   
   ![](../../../../document/function/Dataset/insertData/insertData-step-4.png?raw=true)
   
4. Define the tel, name and add.
   <br>
   tel: 34345678<br>
   name: 111<br>
   add: abc<br>
   
   ![](../../../../document/function/Dataset/insertData/insertData-step-5.png?raw=true)
   
5. Call the function "loadData"and define the         dataset.<br>
   dataset: customer_1<br>
   
   ![](../../../../document/function/Dataset/insertData/insertData-step-6.png?raw=true)
   
6. Add a console after callback for display the       response from console.

   ![](../../../../document/function/Dataset/insertData/insertData-step-7.png?raw=true)
  
### Result

 ![](../../../../document/function/Dataset/insertData/insertData-result-1.png?raw=true)
 
  ![](../../../../document/function/Dataset/insertData/insertData-result-2.png?raw=true)
 
## Notes

- N/A