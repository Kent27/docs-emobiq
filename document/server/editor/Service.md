# Service

## Description

This page contains the Connectors and Services that will be used in the generated application.

Access this page through the service menu in the toolbar.

![Service Menu](service-menu.png?raw=true)

## Supported Services

The menu on the left side displays the supported Services, currently this includes:

- **RAW(REST) Connector:** used as a connector for REST endpoints which parameter includes:
    - Name: identifier of the connector
    - Url: endpoint of the Rest Endpoint
    - Timeout: the configuration for the duration before the api times out
- **SOAP Connector:** used as a connector for API using SOAP approach.
    - Name: identifier of the connector.
    - Url: endpoint of the SOAP Endpoint.
    - Timeout: the configuration for the duration before the api times out.
- **Database Connector:** used as a connector to the Database that is created on Database Module and will be generated upon running the application.
    - Name: identifier of the connector.
    - Database: selection of database that has been created on the Database module.
- **Database Table Connector:** used as a connector to the Database Table that is created on Database Module and will be generated upon running the application.
    - Name: identifier of the connector
    - Database: selection of database that has been created on the Database module
    - Table: selection of table that has been created on the Database module
  
![Supported Services](service-supported.png?raw=true)

## Sample of Created Services
  
![Services Example](service-example.png?raw=true)