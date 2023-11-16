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
                
   ![](./insertData-step-1.png)
   
   ![](./insertData-step-2.png)
   
2. Create a dataset is  in Services.
   <br>
   dataset: customer_1<br>
   
   ![](./insertData-step-3.png)

3. Call the function "insertData", define the         dataset and set function "toObject"to              param.
   <br>
   dataset: customer_1<br>
   param: toObject<br/>
   
   ![](./insertData-step-4.png)
   
4. Define the tel, name and add.
   <br>
   tel: 34345678<br>
   name: 111<br>
   add: abc<br>
   
   ![](./insertData-step-5.png)
   
5. Call the function "loadData"and define the         dataset.<br>
   dataset: customer_1<br>
   
   ![](./insertData-step-6.png)
   
6. Add a console after callback for display the       response from console.

   ![](./insertData-step-7.png)
  
### Result

 ![](./insertData-result-1.png)
 
  ![](./insertData-result-2.png)
 
## Notes

- N/A