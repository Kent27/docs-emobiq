# componentMethod

## Description

To trigger a built an method/function within the component.

The component mentioned in this function refers to both page components and services.

To know the methods available for the component, please check the specific component documentation.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component to trigger the method from. | Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId |  The id of the component to trigger the method from.| Text | - | - | Partial (Yes if no 'component'.) |
| method | The method to be triggered from the component. | Text | - | - | Yes |
| arguments | The arguments/paramters to be used for the method. | Array/List | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the result based on the method called, if the component is not found it returns 'false'. | Any |

Note: This can also have side effects to the components, depending on the method called.