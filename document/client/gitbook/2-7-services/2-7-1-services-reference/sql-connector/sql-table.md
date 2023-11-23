# SQL Table

The following fields are used in the SQL Table to configure SQL queries and data retrieval. These fields control various aspects of data exchange and querying within your SQL database.

## Name
- **Description**: The user-defined identifier for the specific configuration or table instance.
- **Type**: Text (string)
- **Example**: "UserDataSQLTable"

## Connector
- **Description**: Specifies the SQL connector being used to interface with the database.
- **Type**: Text (string)
- **Example**: "SQLConnectorV2"

## Select
- **Description**: Specifies the columns to be selected in the SQL query.
- **Type**: Text (string)
- **Example**: "user_id, username, email"

## From
- **Description**: Specifies the table from which to retrieve data in the SQL query.
- **Type**: Text (string)
- **Example**: "Users"

## Where
- **Description**: Specifies the conditions for filtering data in the SQL query.
- **Type**: Text (string)
- **Example**: "age > 18"

## Group
- **Description**: Specifies the columns by which to group the data in the SQL query.
- **Type**: Text (string)
- **Example**: "gender"

## Limit
- **Description**: Specifies the maximum number of records to be retrieved in the SQL query.
- **Type**: Numeric (integer)
- **Example**: 50

## Listkey
- **Description**: A unique identifier or key associated with a specific list or dataset in the SQL table.
- **Type**: Text (string)
- **Example**: "UsersList"

## Autoload
- **Description**: A boolean value (true/false) that indicates whether data from this table should be loaded automatically onto the datalist component. This setting applies only once, during the initial loading of the datalist on page load event. Note that the table must be linked to a datalist component within a page before enabling this option.
- **Type**: Boolean
- **Example**: true
