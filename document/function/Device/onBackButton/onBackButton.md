# onBackButton

## Description

Triggers the back button to navigate to another page. This is applicable to android devices only.

## Input / Parameter

N/A

## Output

N/A

## Callback

### callback

The function to be executed when the back button is triggered to navigate to the page specified successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user wants to redirect to another page when they press the back button.

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](../onBackButton/onBackButton-step-1.png?raw=true) | Drag a button to a page in the mobile designer. Select the event `click` for the button and drag the `onBackButton` function to the event flow. |
| 2. | ![](../onBackButton/onBackButton-step-2.png?raw=true) | Drag the function to be executed when the back button is triggered. In this example, we are using the `gotoPage` function. |
| 3. | ![](../onBackButton/onBackButton-step-3.png?raw=true) | Select the page to navigate to. |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}?raw=true) -->

### Result

When the back button is pressed, the current page will redirect to pgWelcome.

<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links