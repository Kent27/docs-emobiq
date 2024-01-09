# Services

eMOBIQ Services allows you to integrate external systems and data sources into your applications. Through eMOBIQ Services, you can establish connections, manage APIs, and structure data with minimal effort. This documentation will guide you through the process of utilizing the "Services" section effectively.

## 1. Introduction to Services

The "Services" section acts as a bridge between your applications and external data sources. It consists of two key components: **Connectors** and **Tables**.

- **Connectors:** These serve as the communication link between your application and external systems or data sources. You can configure the connection settings, authentication details, and API endpoints through connectors.

- **Tables:** Tables are data structures that define how data from external sources is organized within your application. Each table corresponds to a connector and represents a specific data entity.

## 2. Accessing the Services Section

To access the "Services" section:
1. Open the eMOBIQ development interface.
2. Look for the "Services" tab and click on it.

## 3. Connectors

### 3.1 Understanding Connectors

Connectors define the type of external system or data source you wish to connect to. Connectors encapsulate data exchange protocols, authentication requirements, and API endpoint configurations, streamlining integration complexities. By creating specific connectors for different APIs and services, you effortlessly extend your application's capabilities to interact seamlessly with external data. eMOBIQ supports a wide range of connectors for various APIs and services.

### 3.2 Adding a Connector

To add a new connector:
1. In the "Services" section, select the desired connector type from the list and drag it into the working area.
2. Click the connector to expand its configuration settings, which includes API endpoints, authentication credentials, and other relevant parameters.
3. Edit and save the connector configuration.

### 3.3 Configuring Connector Settings

When configuring a connector, ensure you have the required authentication details and API documentation. These settings might include API keys, access tokens, endpoints, and more.

### 3.4 Editing Connectors

To edit a connector:
1. Locate the connector in the Services space.
2. Click to expand and edit. You may also choose to duplicate or remove the connector.

## 4. Tables

### 4.1 Working with Tables

<!-- Tables define how data from connectors is organized within your application. There are two kinds of tables: erp tables and memory tables. Typically, each table corresponds to a specific connector and represents a distinct data source. You can also use memory tables provided by local table and sqlite using relevant actions to cache the incoming data. -->
Tables in eMOBIQ organize data from connectors. There are two types of tables: webservice tables (e.g. ERP tables) and memory tables. Typically, each table corresponds to a specific connector, representing a unique data source. You can also use memory tables, created via local tables or SQLite, to cache incoming data.

Note:

    Additionally, please be aware that besides using Tables to organize data, you can also leverage specific call actions (e.g., `navCall`) in the visual logic of your application. These actions allow you to interact with a configured connector (e.g., NAV Connector) to retrieve data directly, providing you with even greater flexibility in data integration.


### 4.2 Creating a New Table

To create a new table:
1. In the "Services" section, select the desired table type from the list and drag it into the Services space.
2. Click on the table to configure its settings. You may refer to the services reference for different configuration descriptions.

Note: Webservice tables directly configured with an endpoint url will automatically retrieve data from the external data source based on the given configuration when you use the `loadData` action.

### 4.3 Mapping Data to Memory Tables

<!-- Data from connectors is mapped to tables automatically based on the table's configuration. Apart from the self-defined table structure of Local table and SQLite table, incoming data within other tables conforms to the table configuration, but do not have a fixed data structure. -->

Data is typically retrieved from either webservice tables using `loadData`, or `rawCall` with a connector. To cache or store incoming data, memory tables (i.e. local table and SQLite) are used. The structure of Local and SQLite tables is user-defined. If the data inserted into the table contains fields that were not defined by the user, the table will automatically include those additional fields.

To insert data from external services into a memory table, it must match the format specified by the table.
For example, consider a Local table with the following structure defined in JSON format:

    {
        "name": "text",
        "age": "integer",
        "height": "integer"
    }
If you want to store data in this Local table, the data retrieved from the source should be in JSON format that conforms to the defined stucture as illustrated below:

    [
        {
            "name": "John Doe",
            "age": 30
            "height": 181
        },
        {
            "name": "Sally",
            "age": 20
            "height": 170
        }
    ]


<!-- For instance, if you want to store 'name' data fields from a data source in a local table, the table must have a 'name' column. Additionally, the data source should include 'name' as a key for successful insertion. -->

This ensures that data is seamlessly integrated into memory tables, maintaining consistency with the table's defined structure.

### 4.4 Working with memory tables

The local table and SQLite table are memory tables in eMOBIQ that you can make use of to cache or store data. To configure a local table or SQLite table structure:
1. Locate the table.
2. Click the table to open its configuration.
3. Adjust the fields, data types, or other settings as needed.

### 4.5 Editing Tables

To modify, delete or duplicate a table:
1. Find the table within the work space.
2. Click to expand and edit.
3. To copy or delete the table, click on the respective "Copy" or "Delete" icon associated with the table then confirm your action.

## 5. Best Practices

- **Plan Ahead:** Determine your integration needs and data structure before adding connectors and tables. Use local table to combine data and manage them easily.
- **Stay Organized:** Use descriptive names for connectors and tables to maintain clarity.
- **Review API Documentation:** Familiarize yourself with the API documentation for each connector to configure settings correctly.
