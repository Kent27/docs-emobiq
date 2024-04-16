# App.getComponentValue

## Description

Returns the value of the component specified by the user. The component value can be displayed in another component using the [`setComponentValue`](./setComponentValue) function.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component that the value is retrieved from. | String/Text | - | - | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the value of the component specified. | String/Text |

## Callback

N/A

## Video


## Example

In this example we will get the component value of an input field using `App.getComponentValue` and print it to the console. 


### Steps

1. First we drag an input box onto the page. We will name it "InputBox" with the value "This is an input field"

![](./componentValue-step-1.png)

2. We want to get the value of "InputBox" and display it in the browser console with the help of the `Log.write` helper function. 
   
3. Drag `App.getComponentValue` into the event flow, and specify the name of the component, which in this case is "InputBox".

![](./componentValue-step-2.png)


### Result

- The value of "InputBox" will be displayed in the browser console.

![](./componentValue-step-3.png)