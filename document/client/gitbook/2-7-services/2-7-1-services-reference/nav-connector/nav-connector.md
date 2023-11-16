# NAV Connector

The NAV Connector enables integration with Microsoft Dynamics NAV (Navision), facilitating seamless communication with the NAV system.

## Name
- **Description**: The name of the Navision connector instance.
- **Type**: Text (string)
- **Example**: "NavConnectorInstance"

## Navconnector
- **Description**: The connector server URL being used to enable this service. Not needed if running application locally on device. This field is ignored if Local is set to true. If Local is set to false, and Connector value is blank, eMOBIQ connector server will be used by default.
- **Type**: Text (string)
- **Example**: -

## Type
- **Description**: The type of integration or communication protocol used by the connector.
- **Type**: Text (string)
- **Example**: "odatav4", "soap"

## Authentication
- **Description**: The authentication method used to establish a secure connection with the Navision system.
- **Type**: Text (string)
- **Example**: "basic authentication", "oauth2"

## Local
- **Description**: Indicates whether the connection should be established locally by the device running the application. Setting this option to true means that the connection is made directly with the target API. Setting this option to false means that the connection is made through the connector server specified in the Navconnector parameter. This is usually set to false for preview, and set to true when the project is to be built and deployed.
- **Type**: Boolean (true/false)
- **Example**: true

## Url
- **Description**: The URL or endpoint of the Navision service or API.
- **Type**: Text (string)
- **Example**: "https://navision.example.com/api"

## Company
- **Description**: The name or identifier of the company within the Navision system.
- **Type**: Text (string)
- **Example**: "CompanyABC"

## User
- **Description**: The username or user ID used to authenticate the connector with the Navision system.
- **Type**: Text (string)
- **Example**: "user123"

## Password
- **Description**: The password associated with the user account for authentication.
- **Type**: Text (string)
- **Example**: "secretpassword"

## Tenantid
- **Description**: For multi-tenant systems, this field represents the identifier of the specific tenant.
- **Type**: Text (string)
- **Example**: "tenant123"

## Clientid
- **Description**: The client or application ID associated with OAuth2 authentication.
- **Type**: Text (string)
- **Example**: "client123"

## Clientsecret
- **Description**: The secret key or password associated with the client ID for OAuth2 authentication.
- **Type**: Text (string)
- **Example**: "clientsecretpassword"

## Timeout
- **Description**: The maximum time allowed for the connector to wait for a response from the Navision system before timing out.
- **Type**: Integer (milliseconds)
- **Example**: 15000 (15 seconds)
