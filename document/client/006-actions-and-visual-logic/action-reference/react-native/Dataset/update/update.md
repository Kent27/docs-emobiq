# Dataset.update

## Description

Updates the data from a dataset.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The name of the dataset that is created in Services. | Text | - | - | Yes |
| filter | The filters to be applied. | FilterFormat | - | - | No |
| data | Multiple dynamic attributes with values associated with each attribute. | Object | - | - | Yes |
| extra | The stored value that is passed to all the callbacks. | Any | - | - | No |

### FilterFormat (Object)

The format used for filtering in the parameter `filter`.

| Key | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| operator | Query operators used to filter multiple times. | Text | And | Or, And | No |
| data | Set of rules for another group of queries. | List | - | - | No |

#### data (List)

Will contain a list of one (1) or more objects with the following structure (dataset, operator, value) and contain zero (0) or more objects with the same structure (FilterFormat only). This can be another FilterFormat to create grouped queries.

| Key | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| dataset | The dataset to filter. | Text | - | - | No |
| field | The field to be filtered. | Text | - | - | Yes |
| operator | Operators to be used for specific filtering. | Text | - | Equal, Not_Equal, Is_Null, Is_Not_Null, Greater_Than, Greater_Than_Or_Equal, Less_Than, Less_Than_Or_Equal, Like, Not_Like, In, Not_In, Between, Not_Between | Yes |
| value | The value to perform the query, which depends on the operator. | Any | - | - | No |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| success | Boolean value to denote whether the function was executed successfully. | Text |
| message | The message to print. | Text |
| data | Any additional message or data to print. | Text |

## Callback

### callback

The action performed if this function runs successfully.

| Description | Output Type |
| ------ | ------ |
| Returns the list of updated data from the dataset. | List |

### errorCallback

The action performed if this function does not run successfully.

| Description | Output Type |
| ------ | ------ |
| Returns an error message. | Text |

## Example

The user wants to update `Local Table` data from their local storage, (this example will only works after the user has created the data using `Dataset.insert` function).

### Steps

1. Make sure the `Local Table` component that's being used in `Dataset.insert` function example is exist and filled on the services panel in the service page. For `fields` field value add `name`and `title` as object key with Text type.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./update-step-1.png"
        style="width: 100%; padding: 5px;"/>
    </div>

2. Drag a button component to a page in the mobile designer.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./update-step-2.png"
        style="width: 50%; padding: 5px;"/>
    </div>

3. Select the event `press` and drag the `Dataset.update` function to the event flow and fill in the parameter, for the `filter` and `data` param change it's type to a function / subflow and put `Conversion.toObject` inside it.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./update-step-3.png"
        style="width: 50%; padding: 5px;"/>
    </div>

4. For the `filter` param change it's type to a function / subflow and put `Conversion.toObject` inside it then add `data` as object key, change it's type to a function / subflow and put `Conversion.toObject` inside it.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./update-step-4.png"
        style="width: 50%; padding: 5px;"/>
    </div>

5. Inside `data` subflow put `Conversion.toObject` inside it then add `field`, `operator`, `value` as object key with `name`, `like`, `n%` as it's value respectively.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./update-step-5.png"
        style="width: 50%; padding: 5px;"/>
    </div>

6. For the `data` param change it's type to a function / subflow and put `Conversion.toObject` inside it then add `title` as object key, with `new value` as it's value.

    <div style="display:flex; align-items:center; justify-content:center; background-color: #E7F1FF;">
        <img src="./update-step-6.png"
        style="width: 50%; padding: 5px;"/>
    </div>

### Result

Should be able to update the data from local storage.