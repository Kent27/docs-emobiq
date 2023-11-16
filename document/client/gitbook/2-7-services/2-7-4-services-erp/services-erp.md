# Connecting to ERP systems (General Guide)

## Data Retrieval

### Step 1: Access the Services

To initiate data retrieval from an ERP system, begin by accessing the services provided by eMOBIQ.

### Step 2: Create and Configure ERP Connector

Create an ERP connector within Services and configure it appropriately. This connector will serve as the link between you application and the ERP system.

### Step 3: Create and Configure ERP Table

Set up an ERP table within Services, ensuring that it is correctly configured to retrieve the specific data from the ERP system.

### Step 4: Select Component and Trigger Event

Choose the component where you want to trigger the data retrieval operation. Select the desired trigger event that will initiate the data retrieval process.

### Step 5: Configure Visual Logic

Navigate to the visual logic section. Within this section, use the `loadData` action in the logic tree to initiate the data retrieval process. Configure this action to load data from the ERP table you previously created. The connection to the external ERP system is automatically established based on the ERP table settings.

### Step 6: Update Operations

Please note that any update operations (made with a separate ERP-specific call action) within the retrieved data will require users to invoke the `loadData` action again to see the latest changes from the ERP system.


## Viewing Data in Datalist

### Step 1: Access the Services

To view data retrieved from the ERP system in a datalist, start by accessing the Services section.

### Step 2: Create and Configure ERP Connector

As in the data retrieval process, create an ERP connector within Services and configure it accordingly to maintain the connection to the ERP system.

### Step 3: Create and Configure ERP Table

Set up an ERP table within Services, ensuring that it is correctly configured to retrieve the specific data from the ERP system.

### Step 4: Create a Datalist Component

Within the visual page editor, create a Datalist component that will display the retrieved data. Configure the properties of this Datalist component as needed.

### Step 5: Add Labels

Drag and drop appropriate labels into the Datalist component. These labels will represent different fields in the retrieved data and will serve as children components within the Datalist.

### Step 6: Map Labels to Data Fields

Map the labels to the desired data fields by specifying the appropriate field attribute. This ensures that the data from the ERP system is correctly displayed in the Datalist.

### Step 7: Finalize Data Presentation

To complete the process, follow steps 4-6 from the "Data Retrieval" section, which involves triggering the data retrieval action and configuring it according to your needs.
