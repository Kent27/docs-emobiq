﻿# chartPopulateDonutData

### Description

A donut chart is essentially a Pie Chart with an area of the centre cut out. 

### Flowchart

- N/A 

### Input / Parameters

| No | Name | Description | Data Type | Required |
| ------ | ------ | ------ |------ | ------ |
| 1 | component | The name of the component that the details will be taken from. | String | Yes |
| 2 | componentId | The id of the component that the details will be taken from. | String | No |
| 3 | title | Title of the chart. | String | Yes |
| 4 | dataCaptions | dataCaptions | Array | Yes |
| 5 | data | Number | Array | Yes |
| 6 | dataColors | dataColors | Array | No |

### Scenario / Use Case

The user wants to create a Donut Chart.

### Step

1. Call the function "chartPopulateDonutData" and define the value          for component, title, dataCaptions, and data.
   <br>
   <ul>
   <li>component: chData</li>
   <li>title: Donut</li>
  
   ![](../../../../document/function/Chart/chartPopulateDonutData/chartPopulateDonutData-step-1.png?raw=true)
   
   <li>dataCaptions: toArray -></li> 
                            <ul>
                            <li>value1: Kevin </li>
                            <li>value2: Ann  </li>
                            <li>value3: Audrey  </li>
                            <li>value4: Nadine </li> 
                            </ul>
   
   ![](../../../../document/function/Chart/chartPopulateDonutData/chartPopulateDonutData-step-2.png?raw=true)
   
   </li><li>data: toArray -></li> 
                          <ul>
                          <li>value1: toArray </li>
                          <ul>
                          <li>value1: 5 </li>
                          <li>value2: 1 </li>
                          <li>value3: 2 </li>
                          <li>value4: 5 </li>
                          </ul>
                          <li>value2: ...... </li>
                          </ul>
                            
   ![](../../../../document/function/Chart/chartPopulateDonutData/chartPopulateDonutData-step-3.png?raw=true)
  
### Result

 ![](../../../../document/function/Chart/chartPopulateDonutData/chartPopulateDonutData-result-1.png?raw=true)
   
 
### Video

- N/A

<!--[![Video](http://i.imgur.com/Ot5DWAW.png)](https://youtu.be/StTqXEQ2l-Y?t=35s)-->

### Notes

- N/A