# Device.mapSetCenter

## Description

Set the center position based on the latitude and longitude provided.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the map component. | Text | - | - | Yes |
| coordinate | The latitude and longitude of the point to set as center. Format: latitude,longitude | Text | - | - | - |

## Output

N/A

## Example

The user wants to set their Map component coordinate by using setMapCenter function

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](./mapSetCenter-step-1.png) | Make sure Map component is exist on the page and add a button component on that page |
| 2. | ![](./mapSetCenter-step-2.png) | Select the event `press` for the button and drag the function `Device.setMapCenter` to the event flow. |
| 3. | ![](./mapSetCenter-step-3.png) | Fill in the parameters of the function. |

### Result

The center of the Map component will be moved following the coordinate from `Device.setMapCenter` function

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links