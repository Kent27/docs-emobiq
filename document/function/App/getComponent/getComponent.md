# getComponent

## Description

Retrieves the details of a component.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component. | String/Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the component. | String/Text | - | - | Partial (Yes if no 'component'.) |

__\* Note:__ Either component or componentId must have value in order for this function to work.

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the details of the component. | Array/List |

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user view all the attribute/ details of a component.

### Step

1. Draw a button "ButtonGetCom".

    ![](../../../../document/function/App/getComponent/getComponent-step-1.png?raw=true)
    
3. Call the function.

    ![](../../../../document/function/App/getComponent/getComponent-step-2.png?raw=true)

### Result

In the console, the details of component:

![](../../../../document/function/App/getComponent/getComponent-result-1.png?raw=true)


## Links