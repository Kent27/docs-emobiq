# Object.setAttribute

## Description
Sets an object’s attribute.

## Input / Parameter
| Name          | Description                         | Input Type  | Default | Options     | Required |
| ------------- | ----------------------------------- | ----------- | ------- | ----------- | -------- |
| object        | The object to set attribute for.    | Object      | -       | -           | Yes      |
| attribute     | The attribute to set.               | String      | -       | -           | Yes      |
| value         | The value to set for the attribute. | Any         | -       | -           | Yes      |

## Output
| Description                                          | Output Type |
| ---------------------------------------------------- | ----------- |
| Returns true or false.  | Boolean   |

## Example
In this example, we will add new attribute to an object.

### Step
1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button.
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setAttribute-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

2. Drag the `Log.write` function to the event flow and change the param type to function.
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setAttribute-step-2.png"
        style="width: 100%; padding: 5px;"/>
    </div>

3. Put `Object.setAttribute` function inside the `value` parameter of the `Log.write` function. Fill in the parameters of the `Object.setAttribute` function.
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setAttribute-step-3.png"
        style="width: 100%; padding: 5px;"/>
    </div>

4. For the object param, we will create a new object using `Conversion.toObject` function.
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setAttribute-step-4.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result
1. This function will return updated object based on new parameter and value.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./setAttribute-step-result.png"
        style="width: 100%; padding: 5px;"/>
    </div>