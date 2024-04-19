I want to create a documentation for my no-code platform, called eMOBIQ.
This section is called callbacks.
Callbacks are constructs in eMOBIQ that primariy serves 2 purpose: to ensure that there is a sequential order of logic execution after waiting for an asynchronus action to complete; and to directly pass data to another logic block in the callback after completion.
Callbacks here are conceptually the same as those used in javascript. Explain this concisely and ensure the explanation is self-contained.
Some logic blocks in eMOBIQ have callbacks. 
These callbacks are represented visually in our visual logic as named arrows. Example "yesCallback" or "noCallback"
Given a logic block with callback feeature, user can add another logic block to the first logic block as the callback. There will be a prompt to ask whether it should be a callback logic block. If "same level" is selected, that means the newly added logic block is not added as a callback logic, and instead it sits on the same level as the asynchronous logic block to be executed concurrently.

Example of when callback is used:
Using the 'rawCall' logic block to initiate a get request from a webservice.
'rawCall' is an asynchronous non-blocking logic, allowing logic blocks on the same level to also execute concurrently.
Lets say there is a 'setVar' logic block used as the yesCallback of 'rawCall'.
To illustrate guarantee of sequence of execution: 'setVar' will not execute until 'rawCall' is done.
To illustrate directly relaying data to callback logic: 'setVar' can directly get the data from 'rawCall' through 'input' and 'extra' parameter typees
