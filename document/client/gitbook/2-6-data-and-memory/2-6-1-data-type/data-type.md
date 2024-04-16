# Data Type

## Introduction

**Data type** defines the structure and nature of the data that can be used and manipulated within the platform. This documentation provides an overview of the data types supported by eMOBIQ, including primitives and composites, how to reference data using variables, the validation mechanisms in place, and the distinction between dynamic and static data.

## Supported Data Types

### Primitive Data Types

1. **Text:** Represents alphanumeric characters and strings of text.
2. **Number:** Represents numeric values, including integers and floating-point numbers.
3. **Boolean:** Represents binary values, either *true* or *false*.
4. **List:** Represents an ordered collection of elements, which can be of any data type, including other lists.

### Composite Data Types

1. **Objects (Key-Value Pairs):** Composite data type that consists of a collection of key-value pairs. Each key is a text identifier, and each value can be of any supported data type, including other objects.

## Referencing Using Variables

Data can be stored and referenced using variables via the `setVar` and `getVar` actions in eMOBIQ. Variables serve as placeholders for actual data values and allow for dynamic manipulation of data throughout the application. eMOBIQ variables can accept any data type without the need to declare the type beforehand. This flexibility enables you to work with a wide range of data without strict type constraints.

When working with variables in eMOBIQ, consider the following points:

- **Dynamic Typing:** eMOBIQ employs dynamic typing for variables, allowing them to hold different data types at different points in the application's execution.

- **Simplified Workflow:** By not requiring explicit type declarations, the platform aims to simplify the workflow for users who may not have strong programming backgrounds.

- **Potential Trade-offs:** While dynamic typing provides flexibility, it is important to be cautious about potential runtime errors that might occur due to unexpected data types.


<!-- ## Validation

eMOBIQ provides mechanisms for data validation, ensuring that the data entered or manipulated adheres to predefined rules and constraints. Depending on the selected data type, the validation can include checks for data format, range, presence, or custom-defined rules. -->

## Dynamic vs Static Data

### Dynamic Data

Dynamic data in eMOBIQ refers to information that can change during the runtime of the application. It allows for adaptability and real-time updates. Dynamic data can be particularly useful when dealing with data that needs to be frequently updated or retrieved from external sources. Example of dyamic data assignment is illustrated by the use of `setVar` during runtime.

### Static Data

Static data in eMOBIQ remains constant throughout the application's execution. It is typically used for fixed values or configuration settings that do not change during runtime. For instance, hard-coded component configurations showcase static data, as these values stay constant during runtime.

## Type Safety Considerations

Type safety refers to the practice of ensuring that the correct data types are used in every context, preventing unintended errors and behaviors during runtime. While the eMOBIQ platform offers the flexibility of working with various data types, it is essential to be mindful of type safety when designing and building your applications. 

### The 'any' Data Type

In addition to the predefined primitive and composite data types, eMOBIQ introduces the concept of the 'any' data type for inputs to actions. The 'any' type is designed to be flexible, allowing you to work with different data types without strict type checking. While the 'any' type can offer convenience, it comes with certain risks and considerations:

- **Lack of Type Checking:** When using the 'any' type, the platform does not enforce strict type checking at compile time. This means that you might encounter runtime errors due to unexpected data types being used in certain contexts.

- **Debugging Complexity:** Errors related to data type mismatches might not become apparent until runtime. This can lead to increased debugging complexity and potentially harder-to-identify issues.

- **Readability and Maintainability:** Actions that heavily relies on the 'any' type can become less predictable, as the data types and action behaviour can change at runtime.

### Best Practices for Type Safety

To ensure the reliability and maintainability of your applications, consider the following best practices regarding type safety:

<!-- 1. **Explicitly Define Types:** Whenever possible, use the predefined primitive and composite data types offered by eMOBIQ. Explicitly defining types enhances code clarity and reduces the likelihood of runtime errors.

2. **Limit 'any' Usage:** While the 'any' type can be convenient in certain situations, use it sparingly and only when absolutely necessary. Be aware of the potential risks associated with its usage. -->

1. **Type Checks and Validation:** Implement runtime checks and data validation such as `isNumber` or `isArray` to verify that data matches the expected types before performing operations. This can help catch type-related errors early.

2. **Documentation and Comments:** Clearly document the expected data types for variables, functions, and other elements in your application. Use comments to explain any complex or potentially ambiguous type usage.

<!-- ### Conclusion

Type safety plays a crucial role in ensuring the stability and reliability of your applications built on the eMOBIQ platform. While the 'any' type offers flexibility, it's important to balance this with the need for clear code, maintainability, and prevention of runtime errors. By following best practices and being mindful of type safety considerations, you can create robust and dependable applications that leverage the platform's capabilities effectively. -->
