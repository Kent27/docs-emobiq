# AWS DynamoDB Table

The following fields are used in the AWS DynamoDB table for integration with the DynamoDB database. These fields control various aspects of data exchange between your application and DynamoDB.

## Name
- **Description**: The user-defined identifier for the specific configuration.
- **Type**: Text (string)
- **Example**: "DynamoDBConfig01"

## Connector
- **Description**: Specifies the AWS DynamoDB connector being used.
- **Type**: Text (string)
- **Example**: "DynamoDBConnectorV2"

## Table
- **Description**: The name of the DynamoDB table you are connecting to.
- **Type**: Text (string)
- **Example**: "MyDataItemsTable"

## Limit
- **Description**: Specifies the maximum number of records that can be fetched in a single query.
- **Type**: Numeric (integer)
- **Example**: 50

## Autoload
- **Description**: A boolean value (true/false) that indicates whether data from this table should be loaded automatically onto the datalist component. This setting applies only once, during the initial loading of the datalist on page load event. Note that the table must be linked to a datalist component within a page before enabling this option.
- **Type**: Boolean
- **Example**: true
