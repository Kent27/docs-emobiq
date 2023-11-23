# Signature Component

The 'Signature' component allows users to capture and display signatures.

## Properties

| Property       | Value Sample | Value Type | Description                                                                 |
|----------------|--------------|------------|-----------------------------------------------------------------------------|
| Name           | signature1   | string     | Specifies the name or identifier of the Signature component.                |
| Value          |            | string     | The captured signature value.                                               |
| Field          | data_field   | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The value contained within this field of the data source will be assigned to the 'Value' property of this component.   |
| Read Only      | false        | boolean    | If set to true, the Signature component will be read-only and not editable.  |
| Line Width     | 2            | number     | Specifies the line width for drawing the signature.                         |
| Hide On Print  | false        | boolean    | If set to true, the Signature component will be hidden when printed.         |
| ID Prefix      | signature_   | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and ID Field.    |
| ID Field       | data_id      | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The name identifier of this component will be overwritten by concatenating the ID Prefix and the value in the data source referenced by the ID Field. |
| Style Class    | signature-style | string   | Specifies the style class to be applied to the Signature component.         |

## Related Actions

N/A

## Example Uses

N/A
