# Events

In eMOBIQ, a component or page event capture user or system interactions. Logic can be binded to the different events, enabling you to define how your application responds when such events are triggered. 

This documentation provides an overview of the events that can be utilized within eMOBIQ components. Understanding these events will help you effectively manage user interactions and enhance the functionality of your application.

Also note that custom events can be defined in a plugin component. For custom events, the publisher of the plugin has to provide information or documentation about its usage.

## Event Types

### **click**
- **Description:** Triggered when a user clicks on a component.
- **Use Case:** This event is useful for capturing user interactions such as button clicks, link selections, or general component activation.

### **load**
- **Description:** Fired when a target page or component, along with all its child components, completes loading. This event signifies that the UI properties of the page or component are fully loaded and ready for interaction. Note that functional properties configured in the actions may not be fully ready at this point.
- **Use Case:** Use this event to execute actions upon the successful loading of a target page or component. It's suitable for scenarios where you want to ensure that all UI elements are present and accessible before performing further interactions or operations. Keep in mind that while the UI is loaded, certain functional aspects, such as data fetching or dynamic content initialization, might still be in progress.

### **onResume**
- **Description:** Triggered when a user returns to the application after exiting it or switching back to it from another app.
- **Use Case:** This event is suitable for scenarios where a user resumes interaction with the application after a period of absence. You can refresh data, restore the application's state, or resume any paused activities.

### **scrollTop**
- **Description:** Triggered when a user scrolls to the top of the target page or component.
- **Use Case:** Use this event to create behaviors triggered when a user reaches the top of a scrollable component, like displaying a "scroll-to-top" button.

### **onScroll**
- **Description:** Triggered during scrolling within a target page or component.
- **Use Case:** This event is ideal for implementing features that respond to scrolling, such as parallax effects or dynamic headers that change appearance as the user scrolls.

### **scrollBottom**
- **Description:** Triggered when a user scrolls to the bottom of the target page or component.
- **Use Case:** Use this event to load additional content or trigger actions when the user reaches the end of a scrollable area.

### **press**
- **Description:** Occurs when a user physically presses down on the target page or component. This event only works with a touch screen device.
- **Use Case:** This event is useful for capturing initial touch interactions, like selecting an item or holding down a button.

### **receiveMessage**
- **Description:** Triggered when a page or component receives a message or communication from an external url defined in a web frame component. This only works when the web frame component is used within the page.
- **Use Case:** Use this event to enable communication between an external webframe url. You can use it to update components based on messages from the external sources.

### **longPress**
- **Description:** Triggered by a user's extended press of 1 second on a component. This only works with a touchscreen device.
- **Use Case:** This event is suitable for creating actions that require the user to press and hold on a component, such as displaying contextual menus or initiating drag-and-drop interactions.

### **item_click**
- **Description:** Similar to the **click** event, specific to individual items within a component.
- **Use Case:** Use this event to capture clicks on individual items within a larger component, like selecting a specific item from a list.

### **item_press**
- **Description:** Similar to the **press** event, specific to individual items within a component.
- **Use Case:** This event is similar to **press**, but it's targeted at individual items within a component. It's useful for capturing touch interactions on specific list items, for example.

### **item_longPress**
- **Description:** Similar to the **longPress** event, specific to individual items within a component.
- **Use Case:** Similar to **longPress**, but designed for individual items within a component. It can be used for capturing extended presses on specific items, triggering contextual actions.

### **item_sortRelease**
- **Description:** Triggered when an item within a datalist component is released after being sorted. Sorting must be enabled in the component's properties for this event to work.
- **Use Case:** Use this event to respond to sorting interactions within a list or sortable component. You can update the order of items or save changes to the backend.

### **change**
- **Description:** Triggered when the value of an input or selection (e.g. radio button) within a component changes.
- **Use Case:** Use this event to capture user input changes, such as text input, checkbox selections, or dropdown menu selections. It's useful for real-time validation or updating dependent components.

### **focus**
- **Description:** Triggered when a component gains focus or becomes the active element.This is used specifically for edit component.
- **Use Case:** This event is helpful for scenarios where you want to perform actions when a user navigates to or interacts with a specific component, such as showing a keyboard for input fields.

### **lostFocus**
- **Description:** Triggered when a component loses focus or is no longer the active element. This is only available for edit component.
- **Use Case:** Use this event to capture when a user navigates away from a component or input field. It's useful for triggering validation or saving input data.

### **afterLoad**
- **Description:** Triggered after a page or component has finished loading. This is only available for pdf component.
- **Use Case:** Similar to the **load** event, this event occurs after the initial loading of content. It's useful for executing actions that require the complete rendering of the component.

### **error**
- **Description:** Triggered when an error occurs within a component or during a specific action. This is only available for pdf component.
- **Use Case:** This event is essential for capturing and handling errors gracefully. You can display error messages to users, log errors for debugging, or trigger error recovery processes.

### **changing**
- **Description:** Triggered while a user is actively making changes to a component, typically an input. This is only available for edit component.
- **Use Case:** This event is suitable for capturing user input changes as they happen, which can be helpful for real-time feedback or updates.

### **enter**
- **Description:** Triggered when a user presses the "Enter" key while interacting with an edit component. This is only available for pdf component.
- **Use Case:** This event is useful for capturing when a user confirms their input in an edit field by pressing the "Enter" key. It's commonly used for search bars, chat input, or form submissions.
