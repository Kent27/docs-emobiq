# clearData 

## Description

Removes the local table specified from a project.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the dataset to remove. | String/Text | - | - | Yes |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns an empty list. | Array/List |

## Callback?

### callback

The function to be executed if the dataset is removed successfully.

### errorCallback

The function to be executed if the dataset is not removed successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to delete the dataset "l_cart" from local table.

### Step

1. Create a local table "l_cart" and add value     for table.
   <br>
   Fields: item_code<br>
           item_name<br>
           price<br>
           quantity<br>
   
   ![](../../../../document/function/Dataset/clearData/clearData-step-1.png?raw=true)
  
   ![](../../../../document/function/Dataset/clearData/clearData-step-2.png?raw=true)
  
2. Call the function "clearData"and define the     dataset.
   <br>
   dataset: l_cart<br>
   
   ![](../../../../document/function/Dataset/clearData/clearData-step-3.png?raw=true)
   
### Result

![](../../../../document/function/Dataset/clearData/clearData-result-1.png?raw=true)

( Before call the function "clearData, the dataset "l_cart" still storing at local table. )

![](../../../../document/function/Dataset/clearData/clearData-result-2.png?raw=true)

( After call the function "clearData, the dataset "l_cart" was been clear from local table. )



## Links