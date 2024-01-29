# Acumatica Connector

The Acumatica Connector facilitates integration with the Acumatica ERP system, enabling seamless communication with the Acumatica platform.

## Name
- **Description**: The name of the Acumatica connector instance.
- **Type**: Text (string)
- **Example**: "AcumaticaConnectorInstance"

## Type
- **Description**: The type of integration or communication protocol used by the connector.
- **Type**: Text (string)
- **Example**: "rest", "odata"

## Url
- **Description**: The base URL of the Acumatica service or API.
- **Type**: Text (string)
- **Example**: "https://acumatica.example.com"

## Basepath
- **Description**: The base path within the Acumatica API for accessing resources.
- **Type**: Text (string)
- **Example**: "/entity/Default/17.200.001"

## Company
- **Description**: The name or identifier of the company within the Acumatica system.
- **Type**: Text (string)
- **Example**: "CompanyABC"

## Branch
- **Description**: The name or identifier of the branch within the Acumatica company.
- **Type**: Text (string)
- **Example**: "BranchX"

## User
- **Description**: The username or user ID used to authenticate the connector with the Acumatica system.
- **Type**: Text (string)
- **Example**: "acumaticauser"

## Password
- **Description**: The password associated with the user account for authentication.
- **Type**: Text (string)
- **Example**: "acumaticasecretpassword"

## Timeout
- **Description**: The maximum time allowed for the connector to wait for a response from Acumatica before timing out.
- **Type**: Integer (milliseconds)
- **Example**: 15000 (15 seconds)
