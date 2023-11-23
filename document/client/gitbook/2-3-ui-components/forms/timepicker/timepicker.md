# Time Picker Component

The 'Time Picker' component is used to allow users to select a time.

## Properties

| Property       | Value Sample | Value Type | Description                                                                     |
|----------------|--------------|------------|---------------------------------------------------------------------------------|
| Name           | timepicker1  | string     | Specifies the name or identifier of the Time Picker component.                   |
| Value          | 12:00 PM     | string     | The initial value to be displayed in the Time Picker component.                  |
| Format         | h:i A      | string     | The format in which the selected time will be displayed. Default format is h:i A.

h	Hour in 12-hour format	1 – 12

hh	Hour in 12-hour format with a leading zero	01 – 12

H	Hour in 24-hour format	0 – 23

HH	Hour in 24-hour format with a leading zero	00 – 23

i	Minutes	00 – 59

a	Day time period	a.m. / p.m.

A	Day time period in uppercase	AM / PM                        |
| Placeholder    | Select time  | string     | The text to be displayed as a placeholder inside the Time Picker component.      |
| Interval       | 15           | number     | The interval in minutes for the time. Default interval is 60 (in minutes). selection.                                  |
| Min Length     | 5            | number     | The minimum length of the time input field.                                      |
| Max Length     | 10           | number     | The maximum length of the time input field.                                      |
| Style Class    | timepicker-style | string | Specifies the style class to be applied to the Time Picker component.            |
| ID Prefix      | timepicker_  | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and the value in the data source referenced by the ID Field.   |
| ID Field       | data_id      | string     | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The name identifier of this component will be overwritten by concatenating the ID Prefix and the value in the data source referenced by the ID Field. |

## Related Actions

<!-- Empty Related Actions section -->

## Example Uses

![Example Use 1](path/to/screenshot1.png)
_Description or caption for example use 1._

![Example Use 2](path/to/screenshot2.png)
_Description or caption for example use 2._

