# mapRoute

## Description

Display the route on the map from the start position to the end position.

## Input / Parameter 

| Name | Description | Data Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the map component. | String/Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the map component. | String/Text | - | - | Partial (Yes if no 'component'.) |
| mode | The route mode to show. | String/Text | Driving | Driving, Walking, Bicycling, Transit | Yes |
| startLatLng | The latitude and longitude of the start position. | String/Text | - | - | Yes |
| endLatLng | The latitude and longitude of the end position. | String/Text | - | - | Yes |
| waypoints | The waypoints on the route. | Object | - | - | No |

## Output

N/A

Note: The map component will show the route for the mode selected from the start position to the end position.

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

Coming Soon.

<!-- Share a scenario, like a user requirements. -->

### Steps

Coming Soon.

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

Coming Soon.

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links