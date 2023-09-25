# setComponentAttr

## Description

Allows users to set a value to an attribute of a component.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component. | String/Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the component. | String/Text | - | - | Partial (Yes if no 'component'.) |
| attr | The attribute of the component. | String/Text | - | - | Yes |
| value | The value of the attribute. | String/Text | - | - | Yes |

__\* Note:__ Either component or componentId must have value in order for this function to work.

## Output

N/A 

Note: The component will be updated to show the value assigned to the attribute.

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example


The user override a specific atrribute of a component.

### Step

1. Draw an edit text "txtTest", a button "setComponentAttr"

    ![](../../../../document/function/App/setComponentAttr/setComponentAttr-step-1.png?raw=true)
    
3. Call the function

    ![](./setComponentAttr-step-2.png?raw=true)
    
    ![](./setComponentAttr-step-3.png?raw=true)

### Result

The attribute "value" of the edit text "txtTest" will have the value of "abc".

![](../../../../document/function/App/setComponentAttr/setComponentAttr-result-1.png?raw=true)

## Links