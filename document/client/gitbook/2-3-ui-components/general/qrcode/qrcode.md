# QR Code Component

The 'QR Code' component is used to generate and display QR codes based on the provided value.

## Properties

| Property     | Value Sample | Value Type | Description                                                          |
|--------------|--------------|------------|----------------------------------------------------------------------|
| Name         | qrCode1, qrCode2 | string   | Specifies the name or identifier of the QR code component.              |
| Value        | https://example.com | string | The value to encode into the QR code.                                 |
| Logo         | path/to/logo.png | string     | Specifies the path to the logo image to be displayed in the QR code.  |
| Field        | data_url      | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The value contained within this field of the data source will be assigned to the 'Value' property of this component. |
| Style Class  | qr-style     | string   | Specifies the style class to be applied to the QR code component.      |
| ID Prefix   | qr_         | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and ID Field. |
| ID Field    | data_id      | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The name identifier of this component will be overwritten by concatenating the ID Prefix and the value in the data source referenced by the ID Field. |

## Related Actions

N/A

## Example Uses

N/A
