# RAW (REST) Connector

The RAW (REST) Connector enables integration with RESTful APIs, allowing communication with external services.

## Name
- **Description**: The name of the RAW (REST) connector instance.
- **Type**: Text (string)
- **Example**: "RAWRESTConnectorInstance"

## Connector
- **Description**: The connector server URL being used to enable this service. Not needed if running application locally on device. This field is ignored if Local is set to true. If Local is set to false, and Connector value is blank, eMOBIQ connector server will be used by default.
- **Type**: Text (string)
- **Example**: -

## Url
- **Description**: The target URL or endpoint of the external RESTful API.
- **Type**: Text (string)
- **Example**: "https://api.example.com/data"

## Local
- **Description**: Indicates whether the connection should be established locally by the device running the application. Setting this option to true means that the rest connection is made directly with the target API. Setting this option to false means that the rest connection is made through the connector server specified in the Connector parameter. This is usually set to false for preview, and set to true when the project is to be built and deployed.
- **Type**: Boolean (true/false)
- **Example**: false

## Timeout
- **Description**: The maximum time allowed for the connector to wait for a response from the RESTful API before timing out.
- **Type**: Integer (milliseconds)
- **Example**: 10000 (10 seconds)
