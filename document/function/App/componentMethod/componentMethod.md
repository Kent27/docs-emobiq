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

The user wants delete a row the data inside the local table. 

### Step
1. Make sure local table is added to Services, and consist of some data.
 
     ![](../../../../document/function/App/componentMethod/componentMethod-Step-1.png?raw=true)

2. Call Function "ComponentMethod"
 
     ![](../../../../document/function/App/componentMethod/componentMethod-Step-2.png?raw=true)
     
3. fill up the function

     ![](../../../../document/function/App/componentMethod/componentMethod-Step-3.png?raw=true)
     
4. run the function and result is the row with ID : ABC123 is deleted 

![](../../../../document/function/App/componentMethod/componentMethod-Step-4.png?raw=true)
### Result

Coming Soon.

<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links