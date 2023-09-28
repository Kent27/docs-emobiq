# DateTime.difference

## Description

Computes the difference between two dates or datetimes.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| date1 | The date to be subtracted from the second date. | Text | - | - | Yes |
| dateFormat1 | The date and/or time format to use. | Text | yyyy-MM-dd HH:mm:ss | yyy-MM-dd HH:mm:ss, yyyy-MM-dd, HH:mm:ss, y, M, d, h, H, m, s, S, E, z | No |
| date2 | The date to subtract the first date from. | Text | - | - | Yes |
| dateFormat2 | The date and/or time format to use. | Text | yyyy-MM-dd HH:mm:ss | yyy-MM-dd HH:mm:ss, yyyy-MM-dd, HH:mm:ss, y, M, d, h, H, m, s, S, E, z | No |
| interval | The type of time interval to be used to compute the difference. | Text | Days | Days, Years, Months, Weeks, Hours, Minutes, Seconds | No |

### Supported date pattern letters

| Format | Description |
| ------ | ------ |
| y | Represents the year. Use 'yyyy' to represent the full year, and 'yy' to represent the last two digits of the year. |
| M | Represents the month. Use 'MM' to represent the month with a leading zero, and 'M' to represent the month without a leading zero. Use 'MMM' to represent the abbreviated name of the month (e.g., Jan, Feb), and 'MMMM' to represent the full name of the month (e.g., January, February). |
| d | Represents the day of the month. Use 'dd' to represent the day with a leading zero, and 'd' to represent the day without a leading zero. |
| h | Represents the hour in 12-hour format. Use 'hh' to represent the hour with a leading zero, and 'h' to represent the hour without a leading zero. |
| H | Represents the hour in 24-hour format. Use 'HH' to represent the hour with a leading zero, and 'H' to represent the hour without a leading zero. |
| m | Represents the minute. Use 'mm' to represent the minute with a leading zero, and 'm' to represent the minute without a leading zero. |
| s | Represents the second. Use 'ss' to represent the second with a leading zero, and 's' to represent the second without a leading zero. |
| S | Represents the millisecond. Use 'SSS' to represent the millisecond with three digits, and 'S' to represent the millisecond with one, two or three digits. |
| E | Represents the day of the week. Use 'EEE' to represent the abbreviated name of the day (e.g., Mon, Tue), and 'EEEE' to represent the full name of the day (e.g., Monday, Tuesday). |
| z | Represents the time zone. Use 'z' to represent the time zone abbreviation (e.g., PST, GMT), and 'Z' to represent the time zone offset from GMT (e.g., +0800). |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the difference in the date or datetime values based on the type of time interval(s) selected. | Number |

## Callback

N/A

## Video

Coming Soon.

## Example

Coming Soon.

### Steps

Coming Soon.

### Result

Coming Soon.

## Links