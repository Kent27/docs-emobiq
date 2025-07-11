# displaySnippet

## Description

Allows users to decide whether to show or hide a snippet modal on the screen.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| snippet | The snippet to be shown or hidden. | String/Text | - | - | Yes |
| show | To show or hide snippet. | Boolean | true | true, false | Yes |
| effect | The animation effect of the snippet. | String | None | None, Fade, Slide | No |

## Output

Note: The page will be updated to show or hide the snippet.

## Example

In this example, we will show a snippet with slide effect.

### Steps

1. First, we will need to have a snippet to display or hide. Create one under the Snippet tab if you don't have any yet. In this example, we will be using a snippet named `Snippet1`.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./displaySnippet-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

2. Drag in a button, to show the snippet modal. 
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./displaySnippet-step-2.png"
        style="width: 50%; padding: 5px;"/>
    </div>

3. In the event `press` of the button fill in the parameters as shown below for both buttons. 
   
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./displaySnippet-step-3.png"
        style="width: 50%; padding: 5px;"/>
    </div>

### Result

1. Try clicking the show button on either Preview or Compiled App, the snippet modal will be shown and covering the screen. 

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./displaySnippet-result-1.png"
        style="width: 50%; padding: 5px;"/>
    </div>

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./displaySnippet-result-2.png"
        style="width: 50%; padding: 5px;"/>
    </div>

## Links

### Related Information

See also:

- Components
    - [Snippet]()