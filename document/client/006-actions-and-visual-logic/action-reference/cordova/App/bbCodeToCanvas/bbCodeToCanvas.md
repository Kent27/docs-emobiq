# bbCodeToCanvas

## Description

Generates a canvas by following a specific format, canvas are mainly used for printing.

This does not include images, to include please refer to [bbCodeToCanvasSync](./../bbCodeToCanvasSync/bbCodeToCanvasSync.md).

### Platform Supported

- Web
- Mobile

## Input / Parameter

| Name | Description | Data Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| text | The text with a specific format to be drawn in the canvas. See `Text Format` after this table. | Text | - | - | Yes |
| font | The name of the font to be used. | Text | monospace | monospace, ocrb | No | 
| size | The size of the font to be used with the suffix 'px' for pixel. | Text | 23px | - | No | 
| canvasWidth | The width of the canvas. | Number | 576 | - | No | 
| marginTop | The margin top value of the canvas. | Number | 0 | - | No | 
| marginLeft | The margin left value of the canvas. | Number | 0 | - | No | 
| marginRight | The margin right value of the canvas. | Number | 0 | - | No | 
| marginBottom | The margin bottom value of the canvas. | Number | 0 | - | No | 

Text Format

- Bold: ```[b]```The text to apply bold.```[/b]```
- Italic: ```[i]```The text to apply italic.```[/i]```
- Font: ```[font={monospace|ocrb}]```The text to apply the font.```[/font]```
- Size: ```[size={number}]```The text to apply the size.```[/size]```
- Linespace: ```[linespace={number}]```The text to apply the linespace.```[/linespace]```
- Alignment: ```[alignment={left|right}]```The text to apply the alignment, where it will start.```[/alignment]```
- Underline: ```[u]```The text to apply underline.```[/u]```
- Strikethrough: ```[s]```The text to apply strikethrough.```[/s]```

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the html canvas. | [HTMLCanvasElement](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas) |

## Links

### Related Information

See also:
- [Printer.canvasToCPCL](../../Printer/canvasToCPCL/canvasToCPCL.md)

### Alternative Implementation

- [App.bbCodeToCanvasSync](../bbCodeToCanvasSync/bbCodeToCanvasSync.md)