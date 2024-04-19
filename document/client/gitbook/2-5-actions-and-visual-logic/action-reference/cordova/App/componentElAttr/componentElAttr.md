# componentElAttr

## Description

Returns the attribute value of a component's element, such as its value, width, height, and etc.

The attributes are based on [html components](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

To know the specific component element type, please check the specific component documentation.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component to get the element's attribute from. | Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the component to get the element's attribute from. | Text | - | - | Partial (Yes if no 'component'.) |
| attr | The attribute of the component's element. | String/Text | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the attribute value of the component's element, if the attribute is not entered will return 'false'. | Text/Boolean |