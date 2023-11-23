# AX Connector

The AX Connector facilitates integration with Microsoft Dynamics AX (now known as Dynamics 365 Finance and Operations), enabling seamless communication with the AX system.

## Name
- **Description**: The name of the AX connector instance.
- **Type**: Text (string)
- **Example**: "AXConnectorInstance"

## Url
- **Description**: The URL or endpoint of the AX service or API.
- **Type**: Text (string)
- **Example**: "https://ax.example.com/api"

## User
- **Description**: The username or user ID used to authenticate the connector with the AX system.
- **Type**: Text (string)
- **Example**: "axuser"

## Password
- **Description**: The password associated with the user account for authentication.
- **Type**: Text (string)
- **Example**: "axsecretpassword"

## Timeout
- **Description**: The maximum time allowed for the connector to wait for a response from the AX system before timing out.
- **Type**: Integer (milliseconds)
- **Example**: 15000 (15 seconds)
