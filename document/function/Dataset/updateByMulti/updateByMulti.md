# updateByMulti

## Description

Updates records from multiple fields in a dataset.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the local table to update the records from. | String/Text | - | - | Yes |
| first? | ? | String/Text | - | - | No |
| filter | The filters for the field and value to update. | Array/List | - | - | Yes |
| orFilter | Additional filters for the field and value to update. | Array/List | - | - | No |
| data | The data to update the records with. | Object | - | - | Yes |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the updated list of records from the local table. | Array/List |

## Callback?

### callback

The function to be executed if the specified records are updated successfully.

### errorCallback

The function to be executed if the specified records are not updated successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to update the name from ABC to A1A2A3A4 and tel from 1234567 to 1111111111 in dataset "l_customer".

### Step

1. Call the function "updateByMulti" and define the dataset.
   <br>
   dataset: l_customer<br>

    ![](./updateByMulti-step-1.png?raw=true)

   
2. Set toArray and toObject function to filter and define the             value of object.
   <br> filter: toArray --> toObject<br>
        id: 25<br>
        code: C12345<br>
         
 
    ![](./updateByMulti-step-2.png?raw=true)

   ![](./updateByMulti-step-3.png?raw=true)

   ![](./updateByMulti-step-4.png?raw=true)

    
3. Set toObject function to data and define the value of object.
   <br> name: A1A2A3A4<br>
        tel: 1111111111<br>

![](./updateByMulti-step-5.png?raw=true)

  
   
### Result

   ![](./updateByMulti-result-1.png?raw=true)
   ( Before update, the name is ABC and tel is 1234567 )
   
   ![](./updateByMulti-result-2.png?raw=true)
   ( After update, the name changed to A1A2A3A4 and tel is 1111111111 )
   


## Links