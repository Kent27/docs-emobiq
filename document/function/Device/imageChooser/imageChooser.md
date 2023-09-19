# imageChooser

## Description

Selects an image from user's phone storage.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| multiple | The image(s) to choose. | Array/List | - | - | Yes |

## Output

N/A

## Callback

### callback

The setComponentValue function will be executed to show the image chosen in the image component if it exists.

### errorCallback

The function to be executed if the image component does not exist.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->


## Example


The user want display the image by choosing it from gallery/phone storage.

### Step

1. Draw a image component "Image653", a button component "imageChooser". 

    ![](../../../../document/function/Device/imageChooser/imageChooser-step-1.png?raw=true)
    
2. In button event, add imageChooser function as below: 

    ![](../../../../document/function/Device/imageChooser/imageChooser-step-2.png?raw=true)

3. In callback, add a setComponentValue function by giving component as "Image653" & value as an input.

    ![](../../../../document/function/Device/imageChooser/imageChooser-step-3.png?raw=true)

### Result

The image choosen will be displayed in image component.
![](../../../../document/function/Device/imageChooser/imageChooser-result-1.png?raw=true)



## Links