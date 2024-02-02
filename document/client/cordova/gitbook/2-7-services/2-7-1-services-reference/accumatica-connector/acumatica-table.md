# Acumatica Table

The following fields are used in the Acumatica table for integration with the Acumatica system. These fields control various aspects of data exchange between your application and Acumatica.

## Name
- **Description**: The user-defined identifier for the Acumatica table.
- **Type**: Text (string)
- **Example**: "AcumaticaConfig01"

## Connector
- **Description**: Specifies the Acumatica connector being used.
- **Type**: Text (string)
- **Example**: "AcumaticaConnectorV2"

## Service
- **Description**: The name or identifier of the specific service within Acumatica that you're connecting to.
- **Type**: Text (string)
- **Example**: "CustomerDataService"

## Limit
- **Description**: Specifies the maximum number of records that can be fetched in a single API call.
- **Type**: Numeric (integer)
- **Example**: 100

## Autoload
- **Description**: A boolean value (true/false) that indicates whether data from this table should be loaded automatically onto the datalist component. This setting applies only once, during the initial loading of the datalist on page load event. Note that the table must be linked to a datalist component within a page before enabling this option.
- **Type**: Boolean
- **Example**: true
