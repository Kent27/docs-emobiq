# Memory

This section delves into the fundamental memory-related concepts and mechanisms that form the foundation of the visual development approach of eMOBIQ.

## 1. Introduction to Memory

In eMOBIQ, memory management is the foundation for efficient data handling within your projects. Through the use of functions, variables, local storage, and specialized constructs, you can seamlessly manage and manipulate data throughout your application.

## 2. Memory Constructs

### 2.1 Variables

Variables are dynamic placeholders for data storage. In eMOBIQ, variables are non-persistent and have a global scope, making them accessible across all pages of your project. These values can be modified and accessed as needed using the appropriate actions.

Initialization and configuration:

Use `setVar` action in the visual logic tree to declare and initialize the variable.

Associated actions for variables:

    `setVar`, `getVar`, `clearAllVar`, `getVarAttr`

### 2.2 Memory Tables

The local table and SQLite table are both memory tables that are available in the services section. You can create and modify memory tables that are accessible globally via associated actions. This provides a structured approach to store data that persists across different sessions. The local table is typically used to cache memory for temporary use, and can be deleted with a cache clear. On the other hand, SQLite table is typically used for more permenant data storage, and can be deleted with dedicated actions.

Initialization and configuration:

Configured in the 'services' section of eMOBIQ.

Associated actions for memory tables:

Local Table

    `insert`, `filterData`, `dataFromString`, `dataToString`, `dataFieldToArray`, `selectAll`, `selectBy`, `updateBy`, `updateByMulti`, `componentMethod`

SQLite 
    
    `insert`, `filterData`, `dataFromString`, `dataToString`, `dataFieldToArray`, `selectAll`, `selectBy`, `updateBy`, `updateByMulti`, `componentMethod`, `query`, `backupSqlite`, `restoreSqlite`

Comparison between local table and SQLite:

| Type        | Description                        | Example Use Case                   |
|-------------|------------------------------------|-----------------------------------|
| Local Table | Cached in local storage            | Temporary storage for user data   |
| SQLite      | More permanent storage             | Storing configuration settings    |

### 2.3 Component Attributes

Component attributes define configurations for each component. These attributes can be read and modified at runtime using actions, allowing for dynamic adjustments to component behavior based on changing data or conditions.

Associated actions for component attributes:

    `componentAttr`, `setComponentAttr`, `componentElAttr`, `setComponentElAttr`, `componentValue`, `setComponentValue`,  `componentElement`, `getComponent`, `setComponentLink`, `setComponentFocus`

### 2.4 Extra Parameter (Value Relay)

The 'extra' parameter is a unique construct in some actions, designed to facilitate the passing of values from a source action to the callback action. This parameter allows for the transfer of data without relying on variables, ensuring that the callback action have access to specific values needed for their execution. 

Note for use: This is only available for actions with callbacks. Values passed from the source action's 'extra' parameter can be accessed by changing the value type of the callback action input to 'extra' type.

## 3. Memory Scope

Apart from the 'extra' parameter, memory scope for all memory constructs in eMOBIQ operates in a public manner, granting access to data across the application. By utilizing the appropriate action interfaces, you can retrieve and modify memory constructs (excluding extra parameter) as needed.

## 4. Data Persistence

Data persistence refers to the ability of a memory constuct to retain data across sessions. In eMOBIQ, only memory tables exhibit data persistence, ensuring reliable information storage between sessions.

Comparison Table for Data Persistence:

| Memory Type | Data Persistence                          |
|----------------|----------------------------------------|
| Variables      | Non-persistent, data only preserved for the current session. Static data is re-initialized every new session.             |
| Memory Table: Local Table  | Persistent local memory used for caching. Data is preserved across sessions and cleared upon cache clear.      |
| Memory Table: SQLite  | Persistent and permenant local memory used for storing and managing data. Data is preserved across sessions and cleared using specific actions.        |
| Components     | Non-persistent, data only preserved for the current session. Static data is re-initialized every new session.      |

## 5. Abstraction of Memory

Abstraction of memory models in eMOBIQ simplifies complex data structures for users. Through actions and related interfaces, you can interact with variables, local storage, and component attributes without needing to delve into underlying implementation details.

## 6. Best Practices

- Utilize variables for non-persistent, global data storage.
- Leverage memory tables (i.e. local table and sqlite) for persistent, structured data needs.
- Utilize connectors and tables for efficient data exchange with external systems.
- Maximize the use of the 'extra' parameter to facilitate value passing between functions.
- Dynamic adjustments to component behavior can be achieved by modifying component attributes.


## 7. Summary of Memory Constructs

| Interface Type | Description                            | Usage                          |
|----------------|----------------------------------------|--------------------------------|
| Variables      | Store and manipulate data that is only used for current session              | User-specific data storage     |
| Memory Tables  | Local and permanent data storage that needs to be carried over to other sessions.      | Structured data storage        |
| Components     | UI and functional building blocks      | User interface customization  |

<!-- ## 7. Troubleshooting

Explore this section for guidance on common memory-related challenges and their resolutions in the eMOBIQ environment.

## 8. Glossary

An eMOBIQ-specific glossary containing relevant terms and their definitions for quick reference.

## 9. Appendix: Code Examples

Practical examples showcasing the implementation of memory-related concepts in eMOBIQ, tailored to real-world scenarios.

With this tailored memory documentation, eMOBIQ users will be equipped to harness the power of functional programming while efficiently managing data and workflows. Happy building! -->
