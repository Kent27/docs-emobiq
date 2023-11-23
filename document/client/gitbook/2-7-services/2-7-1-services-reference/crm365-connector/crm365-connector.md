# CRM365 Connector

The CRM365 Connector enables integration with Microsoft Dynamics 365 Customer Relationship Management (CRM365), facilitating seamless communication with the CRM365 system.

## Name
- **Description**: The name of the CRM365 connector instance.
- **Type**: Text (string)
- **Example**: "CRM365ConnectorInstance"

## Url
- **Description**: The base URL of the CRM365 service or API.
- **Type**: Text (string)
- **Example**: "https://crm365.example.com"

## Resourceurl
- **Description**: The URL for the specific resource within the CRM365 system.
- **Type**: Text (string)
- **Example**: "https://crm365.example.com/api/resource"

## Authorityid
- **Description**: The authority ID or tenant ID for authentication.
- **Type**: Text (string)
- **Example**: "tenant123"

## Clientid
- **Description**: The client or application ID associated with authentication.
- **Type**: Text (string)
- **Example**: "client123"

## User
- **Description**: The username or user ID used to authenticate the connector with CRM365.
- **Type**: Text (string)
- **Example**: "crmuser"

## Password
- **Description**: The password associated with the user account for authentication.
- **Type**: Text (string)
- **Example**: "crmsecretpassword"

## Apiurl
- **Description**: The specific API URL within the CRM365 system.
- **Type**: Text (string)
- **Example**: "https://crm365.example.com/api"

## Timeout
- **Description**: The maximum time allowed for the connector to wait for a response from CRM365 before timing out.
- **Type**: Integer (milliseconds)
- **Example**: 15000 (15 seconds)

## Testconnect
- **Description**: A command or flag to initiate a connection test with CRM365.
- **Type**: Command or Boolean (true/false)
- **Example**: true
