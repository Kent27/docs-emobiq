# displaySnippet

## Description

Allows users to decide whether to show or hide a snippet on the screen.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| snippet | The snippet to be shown or hidden. | String/Text | - | - | Yes |
| show | To show or hide snippet. | Boolean | true | true, false | Yes |
| effect | The animation effect of the Snippet. | String | None | None, Fade, Slide | No |

## Output

N/A

Note: The page will be updated to show or hide the snippet.

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example



### Steps

1. First, we will need to have a snippet to display or hide. Create one if you don't have any. In this example, we will be using this snippet named `Snippet1`.

    ![](./displaySnippet-step-1.png)

2. Drag in a Snippet component and two buttons, one to hide the snippet and one to show it. 
   
    ![](./displaySnippet-step-2.png)

3. In the event `onClick` of the button fill in the parameters as shown below for both buttons. 
   
    ![](./displaySnippet-step-3.png)
    ![](./displaySnippet-step-4.png)

### Result

Try clicking the hide button first and then the show button in either Preview or Compiled App. 

![](./displaySnippet-result-1.png)
<!-- Explain the output.

Format: ![]({image-path}) -->

## Links