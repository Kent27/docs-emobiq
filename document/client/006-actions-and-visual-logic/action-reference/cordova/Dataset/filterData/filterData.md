# filterData

## Description

Retrieves the data that has been filtered with a specific field name from a local table.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the local table to be filtered. | String/Text | - | - | Yes |
| or? | Filter by all criterias or by any one. | Boolean | false | true, false | No |
| criteria1 | The first criteria to filter the dataset by. | Object | - | - | Partial (Yes if none of the other criterias have value.) |
| criteria2 | The second criteria to filter the dataset by. | Object | - | - | Partial (Yes if none of the other criterias have value.) |
| criteria3 | The third criteria to filter the dataset by. | Object | - | - | Partial (Yes if none of the other criterias have value.) |
| criteria4 | The fourth criteria to filter the dataset by. | Object | - | - | Partial (Yes if none of the other criterias have value.) |
| criteria5 | The fifth criteria to filter the dataset by. | Object | - | - | Partial (Yes if none of the other criterias have value.) |

__\* Note:__ At least one field from criteria1 to criteria5 must have value in order for this function to work.

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the list of filtered records from the local table. | Array/List |

## Callback?

### callback

The function to be executed if the local table is filtered successfully.

### errorCallback

The function to be executed if the local table is not filtered successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->


## Example


The user wants to display the data which name=Memory DDR RAM 8GB in dataset "l_item".

### Step

1. Call the function "filterData" and define the dataset. 
   <br>
   dataset: l_item<br>
  
    ![](./filterData-step-1.png)
   
2. Set toObject function to criteria1 and define by, op and          value.<br>
   by: name<br>
   op: =<br>
   value: Memory DDR RAM 8GB
   
   ![](./filterData-step-2.png)
    
### Result

 ![](./filterData-result-1.png)



## Links