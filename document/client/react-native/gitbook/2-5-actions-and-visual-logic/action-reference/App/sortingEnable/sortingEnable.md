# sortingEnable

## Description

Enables the ability to sort a datalist component. 

## Input / Parameter

N/A

## Output

N/A

## Callback

N/A

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

In this example, we will first create a data list, which can then be made sortable with the `sortingEnable` function.

### Steps

1. First, add a "Enable Sorting" button and a datalsit component to the page. 

    ![](./sortingEnable-step-1.png)

2. To load data into the datalist, we will need to create the following event flow. 

    ![](./sortingEnable-step-2.png)

    a. For the `dataFromString` function

    ![](./sortingEnable-step-3.png)

    | Field | Value | 
    | ---- | ---- | 
    | dataset | l_user |
    | string | ![](./sortingEnable-step-4.png) |

    
    b. For the `loadData` function
    ![](./sortingEnable-step-5.png)

3. Finally, for our "Enable Sorting" button, we will add the `sortingEnable` function when the button is clicked. 

    ![](./sortingEnable-step-6.png)

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

![](./sortingEnable-result-1.gif)

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links