# Image Component

The 'Image' component is used to display images within an interface. It allows dynamic navigation and changing of resource files based on the specified name.

## Properties

| Property         | Value Sample      | Value Type | Description                                                            |
|------------------|-------------------|------------|------------------------------------------------------------------------|
| Name             | imgPhoto, img     | string     | Specifies the name or identifier of the image component.  |
| URL              | App/icons/logo.png | string    | Specifies the destination of the resource file for the image.           |
| External URL     | https://example.com/image.png | string | Specifies the external URL of the image to be displayed.           |
| Hide On Print    | True, False          | boolean    | If set to true, hides the image component when the page is printed.   |
| Style Class      | image-class-name  | string     | Applies a custom style class to the image component.                    |
| ID Prefix   | Cart_, Stock_         | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and ID Field. |
| ID Field    | data_id      | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The name identifier of this component will be overwritten by concatenating the ID Prefix and the value in the data source referenced by the ID Field. |
| Zoom             | true              | boolean    | If set to true, enables zoom functionality for the image.               |

## Related Actions

N/A

## Example Uses

N/A
