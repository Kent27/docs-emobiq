# Edit Component

The 'Edit' component is used to capture and display user input.

## Properties

| Property       | Value Sample | Value Type | Description                                                                     |
|----------------|--------------|------------|---------------------------------------------------------------------------------|
| Name           | edit1        | string     | Specifies the name or identifier of the Edit component.                         |
| Value          | John Doe   | string     | The initial value to be assigned to the Edit component.                        |
| Placeholder    | Enter text | string     | The text to be displayed as a placeholder inside the Edit component.            |
| Type           | text         | string     | Specifies the type of input expected in the Edit component (e.g., text, password). |
| Pattern        | [A-Za-z]+    | string     | Specifies a regular expression pattern to validate the input in the Edit component. |
| Min Length     | 0            | number     | Specifies the minimum number of characters required in the Edit component.      |
| Max Length     | 100          | number     | Specifies the maximum number of characters allowed in the Edit component.       |
| Custom Keyboard| false        | boolean    | If set to true, enables a custom keyboard layout for the Edit component.        |
| Hide On Print  | false        | boolean    | If set to true, the Edit component will be hidden when printed.                  |
| Style Class    | edit-style   | string     | Specifies the style class to be applied to the Edit component.                  |
| Read Only      | false        | boolean    | If set to true, the Edit component will be read-only and not editable.           |
| Disabled       | false        | boolean    | If set to true, the Edit component will be disabled and not interactable.        |
| ID Prefix      | edit_        | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and the value in the data source referenced by the ID Field.   |
| ID Field       | data_id      | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The name identifier of this component will be overwritten by concatenating the ID Prefix and the value in the data source referenced by the ID Field. |

## Related Actions

<!-- Empty Related Actions section -->

## Example Uses

![Example Use 1](path/to/screenshot1.png)
_Description or caption for example use 1._

![Example Use 2](path/to/screenshot2.png)
_Description or caption for example use 2._

![Example Use 3](path/to/screenshot3.png)
_Description or caption for example use 3._

...
