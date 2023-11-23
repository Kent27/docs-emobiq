# Step-by-Step Guide for Services Setup

**Note:** This section assumes that you have an understanding of the key components of eMOBIQ Services. This guide will walk through the steps to set up your application to integrate external systems and data sources:

## 1. Accessing the Services Section

- Open the eMOBIQ development interface.

- Locate the "Services" tab in the interface and click on it to access the Services section.

## 2. Adding Connectors

To connect your application to external systems or data sources, you'll need to add connectors:

- In the "Services" section, look for the list of available connectors.

- Select the desired connector type (e.g., NAV Connector) from the list and drag it into the working area.

- Click on the added connector to configure its settings. This includes specifying API endpoints, authentication credentials, and any other relevant parameters. Ensure you have the necessary authentication details and API documentation handy during this step.

- Edit and save the connector configuration.

## 3. Creating Tables

Tables are used to organize and structure data from connectors within your application. You can create different types of tables:

### 3.1. Webservice Tables (e.g., ERP Tables)

- In the "Services" section, select the type of table you want to create (e.g., NAV Table) from the list and drag it into the Services space.

- Click on the table to configure its settings. You can refer to the services reference for detailed configuration descriptions.

- Webservice tables directly configured with an endpoint URL will automatically retrieve data from the external data source based on the given configuration when you use the `loadData` action.

### 3.2. Memory Tables (Local Table and SQLite)

- To cache or store incoming data, you can use memory tables such as Local Table and SQLite. These tables have user-defined structures.

- To configure a Local Table or SQLite Table:

   a. Locate the table within the workspace.

   b. Click the table to open its configuration.

   c. Adjust the fields, data types, or other settings as needed to define the structure of the table.

- The structure of Local and SQLite tables is user-defined. If the data inserted into the table contains fields that were not defined by the user, the table will automatically include those additional fields.

## 4. Data Retrieval

Data retrieval is a crucial step in your integration process. You have two main options for retrieving data:

- **Option 1: Using `loadData` with Tables**

   - With tables, you can use the `loadData` action to retrieve data from external sources. This action is particularly useful when working with webservice tables configured with endpoint URLs. The `loadData` action will fetch data based on the given table configuration.

- **Option 2: Using Specific webservice/ERP Calls with Connectors**

   - Alternatively, you can use specific ERP calls (e.g., `navCall` or `rawCall`) in the visual logic of your application with a configured connector (e.g., NAV Connector or RAW(REST) Connector) to retrieve data directly from external sources. This method provides more control and flexibility in data retrieval, especially when dealing with complex data integration scenarios.

## 5. Mapping Data to Memory Tables

To store and manage data in memory tables, make sure that the data format matches the structure specified by the table. For example, if you have a Local Table with a defined structure in JSON format, ensure that the incoming data conforms to this structure. You can use the `dataFromString` action to store the retrieved data into a specified memory table. 

## 6. Working with Memory Tables

You can continue to work with memory tables (Local Table and SQLite Table) by modifying, deleting, or duplicating them as needed. To do this:

1. Find the memory table within the workspace.

2. Click to expand and edit its configuration.

3. To copy or delete the memory table, click on the respective "Copy" or "Delete" icon associated with the table, then confirm your action.

By following these steps, you'll have successfully set up eMOBIQ Services to integrate external systems and data sources into your application. This powerful integration capability enhances your application's functionality and allows you to manage data seamlessly.
