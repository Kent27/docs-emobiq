# API - Method

## Description

Each Action can hold five different Methods, and each Method can have different behavior among each other, and can be
configured independently.

![Method tab](Method-tab.png)

## Supported Methods

* **GET**:
    * Description: Used to respond with data requested by the client without making any changes to the server's state.
    * Example use cases:
        * Retrieving data from a database: Fetching user information or product details to send back to the client.

* **PATCH**:
    * Description: Used to apply partial modifications to a resource on the server.
    * Example use cases:
        * Updating user preferences: Applying changes to specific settings within a user's profile without affecting the
          entire profile.
        * Editing content: Modifying specific fields of an article or post without altering the rest of the content.

* **PUT**:
    * Description: Used to either update an existing resource or create a new resource with a specific identifier.
    * Example use cases:
        * Updating existing records: Replacing an outdated version of a product description with a new one in the
          database.
        * Creating resources with specific IDs: Using a PUT request to create a new entry in a catalog with a designated
          product code.

* **POST**:
    * Description: Used to handle data submitted by the client and take appropriate actions based on that data.
    * Example use cases:
        * Processing form submissions: Receiving user inputs like login credentials or feedback and validating them on
          the server.
        * Creating new records: Accepting data for generating new posts, comments, or user profiles and storing them in
          the database.

* **DELETE**:
    * Description: Used to initiate the removal of a resource from the server.
    * Example use cases:
        * Deleting content: Handling requests to remove outdated articles or media files from the server's storage.
        * Deactivating accounts: Processing requests to delete user accounts and associated data, making them no longer
          accessible.

## Note

While strict adherence to the above HTTP methods is not mandatory, it is recommended to follow the standard guidelines when building your API.
