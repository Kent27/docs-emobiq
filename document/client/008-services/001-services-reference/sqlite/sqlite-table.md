# SQLite Table

The SQLite table is a memory table used for data management locally, typically in scenarios involving substantial data volumes. The following fields are used to control various aspects of data exchange and configuration within the SQLite database.

## Connector
- **Description**: Specifies the type or version of the connector being used to interface with the SQLite database.
- **Type**: Text (string)
- **Example**: "SQLiteConnectorV2"

## Name
- **Description**: The user-defined identifier for the specific configuration or table instance.
- **Type**: Text (string)
- **Example**: "UserDataTable"

## Autoload
- **Description**: A boolean value (true/false) that indicates whether data from this table should be loaded automatically onto the datalist component. This setting applies only once, during the initial loading of the datalist on page load event. Note that the table must be linked to a datalist component within a page before enabling this option.
- **Type**: Boolean
- **Example**: true

## Uniquekey
- **Description**: A boolean value (true/false) that indicates whether a unique key constraint should be applied to the data in this table. When set to true, a unique identifier is generated for each record, ensuring data integrity and uniqueness. The unique identifier for each record can be accessed by the generated "_id" column in the table.
- **Type**: Boolean
- **Example**: true

## Fields
- **Description**: Defines the fields or attributes for the SQLite table along with their types. This is represented as a dictionary (object) where each key is a field name and its value is an object containing the field type.
- **Type**: Object
- **Example**: `{"user_id": {"tp": "text"}, "username": {"tp": "text"}, "email": {"tp": "text"}, "age": {"tp": "integer"}}`
