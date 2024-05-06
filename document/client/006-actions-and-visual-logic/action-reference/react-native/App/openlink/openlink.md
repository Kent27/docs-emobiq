# App.openLink

## Description

Opens a link in a new tab in a mobile web browser.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| link | The link to be opened. | String/Text | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| success | Boolean value to denote whether the function was executed successfully. | Text |
| message | The message to print. | Text |
| data | Any additional message or data to print. | Text |

## Example

In this example, we will use the `App.reload` function to open the link for the eMOBIQ dashboard in another tab.

### Steps

1. Drag a button component to the canvas and click on the 'Action' tab.
2. Drag the `App.openlink` function to the event flow under the 'press' event.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./openlink-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

3. Under the inspector of the component, enter the link you want to open. In this example, we are using `https://main.emobiq.com/`, the link to the eMOBIQ dashboard.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./openlink-step-2.png"
        style="width: 50%; padding: 5px;"/>
    </div>

### Result

1. Save and preview the app.
2. Click the button to open the dashboard in another tab.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./openlink-result-1.gif"
        style="width: 100%; padding: 5px;"/>
    </div>