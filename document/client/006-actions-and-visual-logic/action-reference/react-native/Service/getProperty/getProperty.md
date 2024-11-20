# Service.getProperty

## Description

Returns the attribute of a service

## Input / Parameter

| Name     | Description                                   | Input Type  | Default | Options | Required |
|----------|-----------------------------------------------|-------------|---------|---------|----------|
| service  | The name of the service to get property from. | String/Text | -       | -       | Yes      |
| property | The attribute of the service.                 | String/Text | -       | -       | Yes      |

## Output

| Description                          | Output Type |
|--------------------------------------|-------------|
| Returns the property of the service. | String/Text |

## Example

In this example, we will obtain the URL property of a REST connector using `Service.getProperty`. 

### Steps

1. Firstly, create a REST service by going to Service tab and drag it into the middle area

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./getProperty-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

2. Place a Button component on a page to execute the functions
3. On the Action tab, in the click event, Create a `Log.write` function, which will call `Service.getProperty`, and specify the name of the service and property to access (which in this case will be "RESTConnector1" and URL respectively).

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./getProperty-step-2.png"
        style="width: 75%; padding: 5px;"/>
    </div>

### Result

1. When opening preview, the URL attribute of "RESTConnector1" will be displayed in the browser console.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./getProperty-result-1.png"
        style="width: 25%; padding: 5px;"/>
    </div>

## Links

### Related Information

See also:

 - Functions
    - [Service.setProperty](/document/client/gitbook/2-5-actions-and-visual-logic/action-reference/react-native/Service/setProperty/)
