# Date Picker Component

The 'Date Picker' component is used to allow users to select a date from a calendar.

## Properties

| Property       | Value Sample | Value Type | Description                                                                     |
|----------------|--------------|------------|---------------------------------------------------------------------------------|
| Name           | datepicker1  | string     | Specifies the name or identifier of the Date Picker component.                   |
| Value          | 2023-07-01   | string     | The initial date value to be set in the Date Picker component.                  |
| Format         | d-m-Y   | string     | The format in which the selected date will be displayed. Default format is d-m-Y.                         |
| Placeholder    | Select date  | string     | The text to be displayed as a placeholder inside the Date Picker component.      |
| First Day      | Monday       | string     | Specifies the first day of the week in the Date Picker component.                |
| Min Date No.   | 1            | number     | The minimum number of days that can be selected from the current date.           |
| Max Date No.   | 365          | number     | The maximum number of days that can be selected from the current date.           |
| Style Class    | datepicker-style | string | Specifies the style class to be applied to the Date Picker component.            |
| ID Prefix      | datepicker_  | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and the value in the data source referenced by the ID Field.   |
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
