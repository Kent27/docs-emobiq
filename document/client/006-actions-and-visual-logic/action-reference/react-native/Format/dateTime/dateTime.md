# Format.dateTime

## Description

Formats a date, time or datetime to follow certain standard date patterns (e.g. "MM-DD-YYYY")

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| date | The reference date to be formatted. | Text | - | - | Yes |
| currentFormat | The current date format of the date to be formatted. | Text | yyyy-MM-dd HH:mm:ss | yyyy-MM-dd HH:mm:ss, yyyy-MM-dd, HH:mm:ss, y, M, d, h, H, m, s, S, E, z | No |
| newFormat | The new date format to update the current date format. | Text | yyyy-MM-dd HH:mm:ss | yyyy-MM-dd HH:mm:ss, y, M, d, h, H, m, s, S, E, z | No |


### Supported date pattern letters

#### Years:
- `YYYY`: 4-digit year (e.g., 2021)
- `YY`: 2-digit year (e.g., 21 for 2021)

#### Months:
- `MMMM`: Full month name (e.g., January, February)
- `MMM`: Short month name (e.g., Jan, Feb)
- `MM`: Month as a 2-digit number (01 for January)
- `M`: Month as a number (1 for January)

#### Days:
- `DD`: Day of the month as a 2-digit number (e.g., 09)
- `D`: Day of the month as a number (e.g., 9)
- `dddd`: Full day name (e.g., Monday, Tuesday)
- `ddd`: Short day name (e.g., Mon, Tue)

#### Hours:
- `HH`: Hours (24-hour clock) as a 2-digit number
- `H`: Hours (24-hour clock) as a number
- `hh`: Hours (12-hour clock) as a 2-digit number
- `h`: Hours (12-hour clock) as a number

#### Minutes:
- `mm`: Minutes as a 2-digit number
- `m`: Minutes as a number

#### Seconds:
- `ss`: Seconds as a 2-digit number
- `s`: Seconds as a number

#### AM/PM:
- `A`: AM/PM uppercase
- `a`: am/pm lowercase

#### Time Zone:
- `Z`: UTC offset (e.g., +07:00)
- `ZZ`: UTC offset in a compact format (e.g., +0700)

These symbols can be combined in any way to match the format of your input date string. For example:

- `YYYY-MM-DD`: Represents dates like "2021-03-14"
- `dddd, MMMM Do YYYY, h:mm:ss a`: Represents dates like "Sunday, March 14th 2021, 5:30:45 pm"

Remember, the format in parameter `currentFormat` should match the structure of `date` you're parsing.

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted date with the correct pattern. | Text |

## Example

In this example, we will change the format of a date string and print the formatted date in the console.

### Step

1. Drag a `button` component into the canvas and open the `Action` tab. Select the `press` event of the button and drag the `Log.write` function to the event flow.
2. Call the function `Format.dateTime` inside the `Log.write` function.
3. Sample parameters are shown in the picture below.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./dateTime-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

### Result

1. The console will print the formatted date.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./dateTime-result-1.png"
        style="width: 15%; padding: 5px;"/>
    </div>
