# componentValue

## Description

Retrieves the value of the component.

### Platform Supported

- Web
- Mobile

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component that the value is retrieved from. | Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the component that the value is retrieved from. | Text | - | - | Partial (Yes if no 'component'.) |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the value of the component, if unable to returns 'false'. | Text/Boolean |