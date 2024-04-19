# componentAttr

## Description

Returns the attribute value of a component, such as its name, dimensions etc.

The component mentioned in this function refers to both page components and services.

To know the attributes available, please check the specific component documentation.

### Platform Supported

- Web
- Mobile

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component to get the attribute from. | Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the component to get the attribute from. | Text | - | - | Partial (Yes if no 'component'.) |
| attr | The attribute of the component. | Text | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the attribute value of the component, if the attribute is not entered will return 'false'. | Text/Boolean |