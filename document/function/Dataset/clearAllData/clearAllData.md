# clearAllData

## Description

Removes all the local tables in a project, excluding the datasets specified.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| except | The datasets that should not be removed. | String/Text | - | - | No |

## Output

N/A

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to delete all the dataset in a project.

### Step

1. Call the function.
   <br>
   
   ![](../../../../document/function/Dataset/clearAllData/clearAllData-step-1.png?raw=true)
   
### Result

![](../../../../document/function/Dataset/clearAllData/clearAllData-result-1.png?raw=true)
( Before call the function "clearAllData" there have Lcustomer and l_cart in this project.)

![](../../../../document/function/Dataset/clearAllData/clearAllData-result-2.png?raw=true)

![](../../../../document/function/Dataset/clearAllData/clearAllData-result-3.png?raw=true)
( After call the function "clearAllData" the two table have been removed.)



## Links