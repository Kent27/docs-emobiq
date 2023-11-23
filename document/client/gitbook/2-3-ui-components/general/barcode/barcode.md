# Bar Code Component

The 'Bar Code' component is used to generate and display barcodes based on the provided value.

## Properties

| Property       | Value Sample | Value Type | Description                                                               |
|----------------|--------------|------------|---------------------------------------------------------------------------|
| Name           | barcode1     | string     | Specifies the name or identifier of the Bar Code component.                |
| Value          | 1234567890 | string     | The value to encode into the barcode.                                     |
| Field          | data_field   | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The value contained within this field of the data source will be assigned to the 'Value' property of this component. |
| Type           | CODE128      | string     | Specifies the type or format of the barcode.                               |
| Display Text   | True         | boolean    | If set to true, displays the text below the barcode with the encoded value. |
| Style Class    | barcode-style | string     | Specifies the style class to be applied to the Bar Code component.         |
| ID Prefix      | barcode_     | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and ID Field.   |
| ID Field       | data_id      | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The name identifier of this component will be overwritten by concatenating the ID Prefix and the value in the data source referenced by the ID Field. |

## Related Actions

N/A

## Example Uses

N/A
