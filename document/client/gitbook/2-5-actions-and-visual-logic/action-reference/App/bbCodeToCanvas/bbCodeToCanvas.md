# bbCodeToCanvas

## Description

Generates a canvas by following a specific format, canvas are mainly used for printing.

## Input / Parameter

| Name | Description | Data Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| text | The text with a specific format to be drawn in the canvas. See Text Format after this table. | String/Text | - | - | No |
| font | The name of the font to be used. | String/Text | monospace | monospace, ocrb | No | 
| size | The size of the font to be used with the suffix 'px' for pixel. | String/Text | 23px | - | No | 
| canvasWidth | The width of the canvas. | Number | 576 | - | No | 
| marginTop | The margin top value of the canvas. | Number | 0 | - | No | 
| marginLeft | The margin left value of the canvas. | Number | 0 | - | No | 
| marginRight | The margin right value of the canvas. | Number | 0 | - | No | 
| marginBottom | The margin bottom value of the canvas. | Number | 0 | - | No | 

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

N/A

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to generate a canvas and convert it to CPCL printing language to print it.

<!-- Share a scenario, like a user requirements. -->

### Steps

1. Set the data to be printed using the `setVar` function. In this example, we use the `forLoop` and store the result in the variable set.

    ![](./bbCodeToCanvasSync-step-1.png)

2. Call the function `bbCodeToCanvas` and call the function `getVar` in the `text` parameter of the function to generate a canvas using the stored value.

2. Call the function `btPrinterPrint` in the callback of the `bbCodeToCanvas`. Call the function `canvasToCPCL` in the `text` parameter of the `btPrinterPrint` function to convert the canvas to CPCL printing language before printing.

    ![](./bbCodeToCanvasSync-step-2.png)

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result
    
1. The canvas generated will be printed.

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links