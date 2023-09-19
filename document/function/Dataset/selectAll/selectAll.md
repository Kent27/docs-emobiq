# selectAll

## Description

Retrieves all data from a local table.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the local table. | String/Text | - | - | Yes |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns all the fields in the local table. | Array/List |

## Callback?

### callback

The function to be executed if all data is retrieved from the local table successfully.

### errCallback

The function to be executed if all data is not retrieved from the local table successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to display all the data in dataset "l_item".

### Step

1. Call the function "selectAll"and define the        dataset.
   <br>
   dataset: l_item
  
   ![](../../../../document/function/Dataset/selectAll/selectAll-step-1.png?raw=true)
    
2. Executes the callback function and add a console for    display the response from console.
 
   ![](../../../../document/function/Dataset/selectAll/selectAll-step-2.png?raw=true)
    
### Result

 ![](../../../../document/function/Dataset/selectAll/selectAll-result-1.png?raw=true)



## Links