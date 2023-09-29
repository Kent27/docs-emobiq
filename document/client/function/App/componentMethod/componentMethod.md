# componentMethod

## Description

To perform InsertBy, DeleteBy or UpdateBy functions to insert, delete or update data in the local table respectively. 

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the local table. | String/Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the local table. | String/Text | - | - | Partial (Yes if no 'component'.) |
| method | The method to be used to execute the changes in the local table. | String/Text | - | - | Yes |
| arguments | The data to be edited, such as a row in the local table. | Array/List | - | - | Yes |

__\* Note:__ Either component or componentId must have value in order for this function to work.

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the updated list of rows in the local table. | Array/List |

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user wants delete a row of data inside a local table. 

### Step
1. Make sure a local table is added to Services, and consists of some data.
 
     ![](./componentMethod-Step-1.png?raw=true)

2. Call the function "ComponentMethod", and enter the parameters. In this example, we are using the `deleteBy` function, which we would enter in the "method" field.
 
     ![](./componentMethod-Step-2.png?raw=true)
     
     For arguments, we are passing the values "_id" and "2" into "toArray" and back to "componentMethod".

     ![](./componentMethod-Step-3.png?raw=true)
     
3. This will select the row where "_id" is equals to "2" in the "l_data" local table, and delete it. 
  ### Result

The specified row will be removed from the local table. 
<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links