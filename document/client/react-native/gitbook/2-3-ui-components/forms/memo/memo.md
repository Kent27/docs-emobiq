# Memo Component

The 'Memo' component is used to capture and display multiline text input.

## Properties

| Property       | Value Sample | Value Type | Description                                                                     |
|----------------|--------------|------------|---------------------------------------------------------------------------------|
| Name           | memo1        | string     | Specifies the name or identifier of the Memo component.                         |
| Value          | Lorem ipsum dolor sit amet...   | string     | The initial value to be assigned to the Memo component.                        |
| Placeholder    | Enter text | string     | The text to be displayed as a placeholder inside the Memo component.            |
| Column Size    | 3            | number     | Specifies the number of columns (width) for the Memo component.                 |
| Row Size       | 5            | number     | Specifies the number of rows (height) for the Memo component.                    |
| Hide On Print  | false        | boolean    | If set to true, the Memo component will be hidden when printed.                  |
| Style Class    | memo-style   | string     | Specifies the style class to be applied to the Memo component.                  |
| Read Only      | false        | boolean    | If set to true, the Memo component will be read-only and not editable.           |
| Disabled       | false        | boolean    | If set to true, the Memo component will be disabled and not interactable.        |
| ID Prefix      | memo_        | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and the value in the data source referenced by the ID Field.   |
| ID Field       | data_id      | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The name identifier of this component will be overwritten by concatenating the ID Prefix and the value in the data source referenced by the ID Field. |

## Related Actions

N/A

## Example Uses

N/A
