# Conversion.toObject

## Description

Creates an object using the key-value pairs provided or creates a new object.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| {Dynamic} | {Based on user inputs.} | Any | - | - | No |

Note: Dynamic input means that user can add the necessary input required as key-value pairs.

## Output   

| Description | Output Type |
| ------ | ------ |
| Returns the new object with the passed data. | Object |

## Example

In this example, we will create an object and print the result in the console.

### Step

1. Call the function `Conversion.toObject` inside the `Log.write` function.

2. Create the parameter(s) as required inside the `Conversion.toObject` and enter the value(s) for each parameter. In this example, we will create 2 parameters, 'name' and 'age' and enter the values {name: John, age: 27}.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./toObject-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The console will print an object as depicted below.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./toObject-result-1.png"
        style="width: 40%; padding: 5px;"/>
    </div>
