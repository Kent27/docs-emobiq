# Function Name

## Description

Explains the function. What it does and what is it used for?

## Input / Parameter

Display and explain the values passed to the function in a table form.

Example below:

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component. | String | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the component. | String | - | - | Partial (Yes if no 'component'.) |
| text | The text with a specific format to be drawn in the canvas. See Text Format after this table. | String | - | - | No |
| font | The name of the font to be used. | String | monospace | monospace, ocrb | No | 
| canvasWidth | The width of the canvas. | Number | 576 | - | No | 

Text Format

- Bold: ```[b]```The text to apply bold.```[/b]```
- Italic: ```[i]```The text to apply italic.```[/i]```
- Image: ```[img x={number} y={number} width={number} height={number}]```The image to be rendered, a base64 or url.```[/img]```
- Font: ```[font={monospace|ocrb}]```The text to apply the font.```[/font]```
- Size: ```[size={number}]```The text to apply the size.```[/size]```
- Linespace: ```[linespace={number}]```The text to apply the linespace.```[/linespace]```
- Alignment: ```[alignment={left|right}]```The text to apply the alignment, where it will start.```[/alignment]```
- Underline: ```[u]```The text to apply underline.```[/u]```
- Strikethrough: ```[s]```The text to apply strikethrough.```[/s]```

## Output

Display and explain the output of the function.

Example below:

| Description | Output Type |
| ------ | ------ |
| Returns the base64 value | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| filePath | The base64 value. | String |

## Callback

Display and explain the callbacks available for the function.

Example below:

### successCallback

Explain what this callback is for?
A successCallback is executed when a function runs successfully. It takes the result returned by the function as its parameter. ?

| Description | Output Type |
| ------ | ------ |
| Returns the base64 value | Object |

#### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| filePath | The base64 value. | String |

## Video

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

Share a scenario, like a user requirements.

### Steps

Show the steps and share some screenshots.

1. .....

<!-- Format: ![]({image-path}?raw=true) -->

### Result

Explain the output.

<!-- Format: ![]({image-path}?raw=true) -->

## Links

Additional information through links.

- [E-Learing]({url-link})