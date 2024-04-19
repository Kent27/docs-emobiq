# componentElement

## Description

Retrieve the [html element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) of the component.

To know the specific component element type, please check the specific component documentation.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component to retrieve html element from. | Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the component to retrieve html element from. | Text | - | - | Partial (Yes if no 'component'.) |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the html element of the component. | [HTMLElement](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) |