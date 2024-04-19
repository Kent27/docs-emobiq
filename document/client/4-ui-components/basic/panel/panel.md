# Panel Component

The 'Panel' component is used to create a container that groups and organizes other components within an interface.

## Properties

| Property         | Value Sample      | Value Type | Description                                                            |
|------------------|-------------------|------------|------------------------------------------------------------------------|
| Name             | panel1, panel2    | string     | Specifies the name or identifier of the panel component.                |
| Hide On Print    | True, False              | boolean    | If set to true, hides the panel component when the page is printed.     |
| Style Class      | panel-class-name  | string     | Applies a custom style class to the panel component.                    |
| ID Prefix   | Panel_         | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and ID Field. |
| ID Field    | data_id      | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The name identifier of this component will be overwritten by concatenating the ID Prefix and the value in the data source referenced by the ID Field. |

## Related Actions

N/A

## Example Uses

N/A
