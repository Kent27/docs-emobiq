# map

## Description

Loop through all the elements in a list to apply a specific operation to each element. 

Example: loop through a list of numbers to square (operation to be applied) every number.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| values | The list of elements to loop through. | Array/List | - | - | Yes |
| extra | Extra parameters stored and passed to callback. | Any | - | - | No |

## Output

N/A

## Callback

### yesCallback

This will be triggered for every loop that happens within the 'values'.

| Description | Output Type |
| ------ | ------ |
| The current active value within the 'values'. | Any |

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user wants to do a mapping for all the values in an array.

### Step

1. Set the variable "Vmap"
   <br>
   var: Vmap
   
    ![](../../../../document/function/Flow/map/map-step-1.png?raw=true)
    
2. Call the function"toArray" and set the value    for    array.
   <br>
   value1: 11<br/>
   value2: 112<br/>
   value3: 1112<br/>
   value4: 11112<br/>
   
   ![](../../../../document/function/Flow/map/map-step-2.png?raw=true)
     
3. Call the function"map" and "getVar".
   <br>
   var : getVar->Vmap <br />
     
   ![](../../../../document/function/Flow/map/map-step-3.png?raw=true)
      
4. Add a console and display the response from           console.
      
   ![](../../../../document/function/Flow/map/map-step-4.png?raw=true)

### Result

![](../../../../document/function/Flow/map/map-result-1.png?raw=true)



## Links