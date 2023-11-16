# NAV Table

The following fields are used in the "NAV" table for the Navision connector. These fields play a crucial role in facilitating the connection and data exchange between your application and the NAV system. Each table corresponds to one page of data from the NAV connector.

## Name
- **Description**: The user-defined identifier for the specific connection configuration.
- **Type**: Text (string)
- **Example**: "ConnectionConfig01"

## Connector
- **Description**: Specifies the the Navision connector being used.
- **Type**: Text (string)
- **Example**: "NAVConnectorV2"

## Listkey
- **Description**: A unique identifier or key associated with a specific list or dataset retrieved from the NAV connector.
- **Type**: Text (string)
- **Example**: "CustomersList"

## Servicename
- **Description**: The name or identifier of the specific service within the NAV system that you're connecting to.
- **Type**: Text (string)
- **Example**: "CustomerDataService"

## Getdatafunction
- **Description**: Indicates the function or method used to retrieve data from the NAV system.
- **Type**: Text (string)
- **Example**: "getCustomerData"

## Insertdatafunction
- **Description**: Represents the function or API endpoint used to insert data into the NAV system.
- **Type**: Text (string)
- **Example**: "insertCustomerData"

## Updatedatafunction
- **Description**: Points to the function or API endpoint used to update data in the NAV system.
- **Type**: Text (string)
- **Example**: "updateCustomerData"

## Limit
- **Description**: Specifies the maximum number of records that can be retrieved in a single API call.
- **Type**: Numeric (integer)
- **Example**: 50

## Autoload
- **Description**: A boolean value (true/false) that indicates whether data from this table should be loaded automatically onto the datalist component. This setting applies only once, during the initial loading of the datalist on page load event. Note that the table must be linked to a datalist component within a page before enabling this option.
- **Type**: Boolean
- **Example**: true
