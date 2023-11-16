# PayPal Connector

The PayPal Connector enables integration with PayPal payment services, facilitating seamless communication with the PayPal platform.

## Name
- **Description**: The name of the PayPal connector instance.
- **Type**: Text (string)
- **Example**: "PayPalConnectorInstance"

## Environment
- **Description**: The environment or mode in which the connector is configured to operate (e.g., "sandbox" or "production").
- **Type**: Text (string)
- **Example**: "sandbox"

## Connector
- **Description**: The connector server URL being used to enable this service.
- **Type**: Text (string)
- **Example**: "PayPalREST"

## Accesstoken
- **Description**: The access token used for authentication with PayPal services.
- **Type**: Text (string)
- **Example**: "YOUR_PAYPAL_ACCESS_TOKEN"

## Timeout
- **Description**: The maximum time allowed for the connector to wait for a response from PayPal services before timing out.
- **Type**: Integer (milliseconds)
- **Example**: 15000 (15 seconds)
