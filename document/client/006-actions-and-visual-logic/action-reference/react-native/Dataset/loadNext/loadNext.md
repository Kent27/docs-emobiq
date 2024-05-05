# loadNext

## Description

Loads the subsequent records in a dataset after loadData function was run.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the local table to be loaded. | String/Text | - | - | Yes |

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

## Callback

### beforeCallback

The function to be executed if the subsequent records are loaded successfully.

## Example

In this example, we will load the next batch of data from the Local Table and display it in a flatlist component. 

```js
Note: This example will only work after the user has created the data using `Dataset.insert` function.
```

### Steps

1. Make sure a `Local Table` component is created and filled on the services panel in the service page.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./loadNext-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

2. Drag a button component to a page in the mobile designer.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./loadNext-step-2.png"
        style="width: 50%; padding: 5px;"/>
    </div>

3. Drag a `flatlist` component to a page in the mobile designer, and drag a `label` component into the `flatlist` component.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./loadNext-step-3.png"
        style="width: 50%; padding: 5px;"/>
    </div>

4. Fill the `flatlist` component property in the page and fill the `label` component property in the `flatlist` component.  Make sure the `label` component field value matches the key of the data that is being stored in the local table.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./loadNext-step-4.png"
        style="width: 50%; padding: 5px;"/>
    </div>

5. Select the event `press` and drag the `Dataset.loadNext` function to the event flow. Fill in the parameters of the function.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./loadNext-step-5.png"
        style="width: 50%; padding: 5px;"/>
    </div>

### Result

1. The next batch of data should be loaded from the local table and displayed in the flalist component.