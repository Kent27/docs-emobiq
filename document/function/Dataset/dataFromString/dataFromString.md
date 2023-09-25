# dataFromString

## Description

This will replace all the existing records in the local table with the new records. The values inserted must be in a JSON format.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the local table to be edited. | String/Text | - | - | Yes |
| string | The values to be inserted in the local table. | Array/List | - | - | Yes |
| append | Inserts the specified content at the end of a selected element. | String/Text | - | - | No |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the list of records in the local table. | Array/List |

## Callback?

### callback

The function to be executed if the local table is updated with the new records successfully.

### errorCallback

The function to be executed if the local table is not updated with the new records successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to replace all the existing records in the local table with the new ones.</br>

### Step

1. Call the function "dataFromString", set the dataset and set the          function "jsonDecode" to string.<br>
   dataset: l_customer<br />
   string: jsonDecode<br/>
    
    ![](./dataFromString-step-1.png?raw=true)
    
2. Call the function "toArray" and set the function "toObject" to string    and define the id and code.<br>
   string: toObject<br />
   id: 1<br>
   code: C00013<br/>
   id: 2<br>
   code: C00014<br>
   id: 3<br>
   code: C00015<br>
   id: 4<br>
   code: C00016<br>
   
   ![](./dataFromString-step-2.png?raw=true)
   
   ![](./dataFromString-step-3.png?raw=true)
   
   ![](./dataFromString-step-4.png?raw=true)
   
   ![](./dataFromString-step-5.png?raw=true)
   
   ![](./dataFromString-step-6.png?raw=true)
  
    
### Result

![](./dataFromString-result-1.png?raw=true)<br>

![](./dataFromString-result-2.png?raw=true)



## Links