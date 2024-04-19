# animate

## Description

An animation lets a component gradually change from one style to another.

Currently, this function only animates an image downward and slowly fades away.

Note: Only applicable for image component.

### Platform Supported

- Web
- Mobile

## Input / Parameter

| Name | Description | Data Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component to animate. | Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the component to animate. | Text | - | - | Partial (Yes if no 'component'.) | 
| type | Not applicable for now. | Text | - | - | No | 
| startPositionY | Starting y-axis position of the animation. | Number | 0 | - | No | 
| endPositionY | Ending y-axis position of the animation. | Number | 0 | - | No | 
| rotationDegree | Rotation degree of the animation. | Number | 0 | - | No | 

## Output

Note: The component will be updated to show the changes. 

## Example

In this example, the image would move downward and slowly fade away upon clicking on it.

### Steps

1. Drag a new `image` component to the page, under it's properties, update the name to `imgAnimate`.

2. Click the action tab. Select the `click` event of the `image` component.

3. In the event flow, drag the `animate` function. 

4. Update the parameters in the inspector of the `animate` function. 

    ```js
    component: imgAnimate
    startPositionY: 0
    endPositionY: 20
    rotationDegree: 45
    ```

### Result

<div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
    <img src="./animate-result-1.gif" style="padding: 5px;">
</div>