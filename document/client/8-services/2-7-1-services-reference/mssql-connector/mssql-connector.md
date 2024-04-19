# MSSQL Connector

The MSSQL Connector facilitates integration with Microsoft SQL Server databases, enabling seamless communication with MSSQL databases.

## Name
- **Description**: The name of the MSSQL connector instance.
- **Type**: Text (string)
- **Example**: "MSSQLConnectorInstance"

## Url
- **Description**: The URL or IP address of the MSSQL server.
- **Type**: Text (string)
- **Example**: "mssql.example.com"

## Port
- **Description**: The port number on which the MSSQL server is listening.
- **Type**: Integer
- **Example**: 1433

## Database
- **Description**: The name of the database to connect to within the MSSQL server.
- **Type**: Text (string)
- **Example**: "MyDatabase"

## User
- **Description**: The username or user ID used to authenticate the connector with the MSSQL server.
- **Type**: Text (string)
- **Example**: "sqluser"

## Password
- **Description**: The password associated with the user account for authentication.
- **Type**: Text (string)
- **Example**: "sqlsecretpassword"

## Timeout
- **Description**: The maximum time allowed for the connector to wait for a response from the MSSQL server before timing out.
- **Type**: Integer (milliseconds)
- **Example**: 15000 (15 seconds)
