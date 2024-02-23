# loadData

## Description

Loads the data from a local table, staging database or 3rd party connector.

## Input / Parameter

| Name    | Description                                                                       | Input Type | Default | Options | Required |
|---------|-----------------------------------------------------------------------------------|------------|---------|---------|----------|
| dataset | The name of the local table to load data from.                                    | String/Text| -       | -       | Yes      |
| fields  | Specifies which fields to retrieve from the local table.                          | Array/List | -       | -       | No       |
| join    | Details about any tables to be joined with the primary dataset for data retrieval.| Array/List | -       | -       | No       |
| filter  | The filters for the fields and values to retrieve.                                | Array/List | -       | -       | Yes      |
| sort    | Specifies the field and direction for sorting the returned data.                  | Array/List | -       | -       | No       |
| limit   | The number of records to be returned from the local table.                        | Number     | -       | -       | No       |
| page    | The page number for pagination purposes.                                          | Number     | -       | -       | No       |
| extra   | Extra parameters stored and passed to callback.  

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

## Callback?

### callback

The function to be executed if the records are loaded successfully.

### errorCallback

The function to be executed if the records are not loaded successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path})]({url-link}) -->


## Example

Coming Soon.


## Links