# getLocation

## Description

Get the current location details (GPS coordinate) of the device.

## Input / Parameters

| No | Name | Description | Data Type | Required | Example |
| ------ | ------ | ------ |------ | ------ | ------ |
| 1 | timeout | Connection time out period in millisecond | Integer | Yes | 1000, 2000, ...
| 2 | enableHighAccuracy | Enable High Accuracy | Boolean | No |

## Output

## Callback

## Video

## Example

Users want to detect current location from current device.

### Step

1. Call the function. <br />
    timeout: 30000 (connection timeout after 30 seconds)<br />
    enableHighAccuracy: true

    ![](../../../../document/function/Device/getLocation/getLocation-step-1.png?raw=true)
    
2. In callback, add a console -> use input function to view the result.

    ![](../../../../document/function/Device/getLocation/getLocation-step-2.png?raw=true)
    
### Result

User will see the result below in console: <br />
__{__ accuracy: 20 <br />
altitude: null <br />
altitudeAccuracy: null <br />
heading: null <br />
lat: 3.1319238 <br />
latLng: "3.1319238,101.63117249999999" <br />
latitude: 3.1319238 <br />
long: 101.63117249999999 <br />
longitude: 101.63117249999999 <br />
speed: null <br />
timestamp: 1554082377187 __}__


## Links


### Notes

- timeout format is in millisecond (ms).