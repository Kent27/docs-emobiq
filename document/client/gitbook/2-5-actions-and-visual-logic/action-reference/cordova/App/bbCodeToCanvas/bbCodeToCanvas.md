# bbCodeToCanvas

## Description

Generates a canvas by following a specific format, canvas are mainly used for printing.

This does not include images, to include please refer to [bbCodeToCanvasSync](./../bbCodeToCanvasSync/bbCodeToCanvasSync.md).

## Input / Parameter

| Name | Description | Data Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| text | The text with a specific format to be drawn in the canvas. See `Text Format` after this table. | String/Text | - | - | No |
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

A html canvas.