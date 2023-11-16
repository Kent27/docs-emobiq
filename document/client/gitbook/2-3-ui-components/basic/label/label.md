# Label Component

The 'label' component is used to display descriptive text in different contexts. It provides a way to visually represent textual information within an interface.

## Icon

![Label Icon](./label.png)

## Properties

| Property         | Value Sample  | Value Type | Description                                                        |
|------------------|---------------|------------|--------------------------------------------------------------------|
| Name             | lblName       | string     | Specifies the name or identifier of the label component.   |
| Caption          | Full Name     | string     | Displays a descriptive text for the label, providing meaningful context.   |
| Field            | Name          | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The value contained within this field of the data source will be assigned to the 'Caption' property of this component.  |
| Hide On Print    | True, False          | boolean    | If set to true, hides the label component when the page is printed.   |
| Style Class      | image-class-name  | string     | Applies a custom style class to the image component.                    |
| ID Prefix   | Cart_, Stock_         | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and ID Field. |
| ID Field    | data_id      | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The name identifier of this component will be overwritten by concatenating the ID Prefix and the value in the data source referenced by the ID Field. |

## Related Actions

N/A

## Example Uses

N/A
