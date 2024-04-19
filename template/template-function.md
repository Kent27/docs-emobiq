# Function Name

## Description

{Explains the function. What it does and what is it used for?} 

### Platform Supported

- Web
- Mobile

<!-- Note that the Platform Supported section is only applicable to Cordova functions. -->

## Input / Parameter

{Display and explain the values passed to the function in a table form.}

Example below:

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| component | The name of the component. | String/Text | - | - | Partial (Yes if no 'componentId'.) |
| componentId | The id of the component. | String/Text | - | - | Partial (Yes if no 'component'.) |
| text | The text with a specific format to be drawn in the canvas. See Text Format after this table. | String/Text | - | - | No |
| font | The name of the font to be used. | String/Text | monospace | monospace, ocrb | No | 
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

{Display and explain the output of the function.}

Example below:

| Description | Output Type |
| ------ | ------ |
| Returns the base64 value. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| filePath | The base64 value. | String/Text |

## Callback

{Display and explain the callbacks available for the function.}

Example below:

### successCallback

Explain what this callback is for.

| Description | Output Type |
| ------ | ------ |
| Returns the base64 value. | Object |

#### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| filePath | The base64 value. | String/Text |

## Example

{Share a scenario, like a user requirements.}

Example below:

In this example, ...

### Video

<!-- Format: [![Video]({image-path})]({url-link}) -->

### Steps

{Show the steps and share some screenshots if necessary.}

Example below:

1. ...

<!-- Format (if no modification required): ![]({image-path}) -->
<!-- Format (if modifications are required): 
    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="{image-path}" 
        style="width: 100%; padding: 5px;"/>
    </div> -->

2. ...

### Result

{Explain the output.}

Example below: 

<!-- Format: ![]({image-path}) -->

## Links

### Related Information

{Additional information through links.}

Example below: 

- [E-Learning]({url-link})

See also:

{Related functions or components to refer to.}

Example below:

- [Variable.get]({file-path})

### Alternative Implementation

{Alternative ways available to achieve the same results.}

Example below:

- [Variable.get]({file-path})


