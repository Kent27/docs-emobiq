# Conditional Logic

## Introduction
Conditional logic blocks in eMOBIQ are essential constructs that allow you to control the flow of logic execution within your no-code applications. They determine which actions to perform based on specified conditions and the corresponding callback logic. This section provides an overview of using conditional logic blocks in eMOBIQ, explaining their purpose and usage.

## Conditional Logic Block
The conditional logic block is accessible from the list of actions within eMOBIQ, labeled as 'conditional.' It serves as a fundamental building block for implementing decision-making processes in your applications.

### Condition Parameter
To define the conditions for executing specific callback logic, you will use the 'condition' parameter within the 'conditional' block. This parameter allows you to specify the criteria that must be met for the associated logic to be executed. Conditions can be based on variables, user inputs, or any other relevant data points within your application.

For more detailed information on creating callback logic, please refer to the "Callback" section in this documentation.

### Analogous to Traditional Programming
The concept of the conditional logic block in eMOBIQ closely resembles traditional programming constructs like if-else statements. It allows you to create conditional branches in your application's logic, enabling you to handle different scenarios and outcomes effectively.

## Example Usage
Here's a simple example demonstrating how to use the 'conditional' logic block with callbacks for each outcome in eMOBIQ:

1. **Set Variable Value**: Initially, using 'setVar' logic block, set the variable 'varA' to the value '5'.

2. **Conditional Check**: Next, use the 'conditional' logic block to check if 'varA' has the value '5'.

3. **Execute Callback Logic**: Define the callback logic that should be executed when the condition is met (true) or not met (false).

    - If the condition is true (i.e., 'varA' equals '5'), display 'true' on the console.

    - If the condition is false (i.e., 'varA' does not equal '5'), display 'false' on the console.

By following these steps, you create a conditional logic block that checks the value of 'varA' and displays 'true' or 'false' on the console accordingly.

## Conclusion
Conditional logic blocks are a vital component of eMOBIQ, enabling you to add decision-making capabilities to your no-code applications. Whether you need to respond to user inputs, validate data, or create complex branching logic, the 'conditional' block allows you to control the flow of your application with ease. Continue exploring the capabilities of eMOBIQ to build dynamic and interactive experiences for your users.

