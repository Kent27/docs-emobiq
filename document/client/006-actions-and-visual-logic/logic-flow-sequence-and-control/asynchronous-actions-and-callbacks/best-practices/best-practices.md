# Asynchronous Actions: Best Practices

Asynchronous logic blocks play a crucial role in enhancing your app's responsiveness and efficiency. Here are some best practices to consider when utilizing these blocks on eMOBIQ.

## 1. Prioritize User Experience

- **Keep UI Responsive**: Design your logic flows in a way that prevents the app's user interface from freezing or becoming unresponsive during asynchronous operations. This ensures a seamless experience for users interacting with your app.

## 2. Use Callback Logic Wisely

- **Assign Callbacks Strategically**: When using callback logic to sequence actions after asynchronous tasks, ensure that your logic is well-structured. Assign callbacks only when their execution truly depends on the outcome of the asynchronous operation.

## 3. Manage Error Handling

- **Implement Error Handling**: Asynchronous operations can encounter errors, such as network failures or invalid data. Incorporate error handling logic to gracefully manage these scenarios and provide users with meaningful feedback.

## 4. Optimize Performance

- **Minimize Unnecessary Calls**: Avoid making redundant asynchronous calls. Use eMOBIQ tables to store and reuse fetched data when appropriate, reducing unnecessary network requests.

- **Set Reasonable Intervals**: If using timers or intervals within your asynchronous logic, set them according to the needs of your app. Avoid excessively short intervals that might lead to unnecessary load or increased network traffic.

## 5. Beware of Race Conditions

- **Caution with Shared Variables**: When using variables shared between asynchronous operations within the same callback, be cautious of race conditions. A race condition occurs when multiple operations try to modify the same variable concurrently, potentially leading to unexpected results. Consider isolating variable usage when necessary.

## 6. Copying Values to Callback Logic Blocks

- **Sharing Data with 'Extra'**: In some cases, you can pass information from a source asynchronous logic block to a callback logic block using a construct called 'extra'. This value is copied and made available for use in the callback logic block. Since this value is copied, there is no memory overwrite of any variable.

## 7. Simplify Logic Flows

<!-- - **Break Down Complex Tasks**: Divide intricate tasks into smaller, manageable sub-tasks. Each sub-task can be executed asynchronously, promoting a more organized and maintainable logic flow. -->

- **Visualize Logic Flows**: Leverage the visual nature of eMOBIQ to create clear and coherent logic flows. Use comments to distinguish asynchronous blocks and their interactions.

## 8. Test and Iterate

- **Test for Scenarios**: Thoroughly test your logic flows for various scenarios, including successful responses and potential errors. This helps identify any unexpected behavior and ensures the logic works as intended.

- **Iterate Based on User Feedback**: Continuously gather feedback from users of your application and iterate on your asynchronous logic blocks. This ensures that your blocks meet real-world usage needs and expectations.

## 9. Document and Educate

- **Provide Clear Documentation**: Create user-friendly documentation that explains the purpose, usage, and potential challenges of asynchronous logic blocks. Help users understand when and how to use these blocks effectively.
