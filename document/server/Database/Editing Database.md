# Editing Database

## Create Database & Table

To create a new Database or Table,

1. Highlight the database / table where you want to create it, select on root database to create a database or select on database / table to create a table / another table.
   ![Database tree list](Editing-list.png)
2. Press the **Create** button at the middle of the main section.
   ![Database create button large](Editing-create-large.png)
3. Configure database creation.
   ![Database create popup](Editing-database-create-popup.png)
   Charset available:
    * **utf8mb4**
    * **latin1**
   Collation available for **utf8mb4** Charset:
    * **utf8mb4_general_ci**
    * **utf8mb4_unicode_ci**
   Collation available for **latin1** Charset:
    * **latin1_general_ci**
    * **latin1_swedish_ci**
4. The new database will be created inside the root database.
5. Alternatively, press the **Create** button on the top right section while highlighting the database root. The database will be created inside the root database.
   ![Database panel](Editing-panel.png)
6. To create a table, press the **Create** button at the middle of the main section while highlighting any database that user has created.
   ![Table create button large](Editing-create-large.png)
7. Configure table creation.
   ![Table create popup](Editing-table-create-popup.png)
   Engine available:
    * **InnoDB**
    * **MyISAM**
   Charset available:
    * **utf8mb4**
    * **latin1**
   Collation available for **utf8mb4** Charset:
    * **utf8mb4_general_ci**
    * **utf8mb4_unicode_ci**
   Collation available for **latin1** Charset:
    * **latin1_general_ci**
    * **latin1_swedish_ci**
8. The new table will be created inside the highlighted database / on top of the highlighted table.
9. Alternatively, press the **Create** button on the top right section while highlighting a database or a table. The table will be created inside the highlighted database / on top of the highlighted table.
   ![Table panel](Editing-table-panel.png)

## Rename Database & Table

To rename a Database or Table,

1. Highlight the database / table which you want to rename
2. Press the **Rename** button on the top right section.
   ![Database panel](Editing-panel.png)
   ![Table panel](Editing-table-panel.png)
3. Enter a new name for the database or table
   ![Database rename popup](Editing-rename-popup.png)
   ![Table rename popup](Editing-table-rename-popup.png)
4. The new name will then be used.

## Delete Database & Table

To delete a Database or a Table,

1. Highlight the database or table which you want to remove.
2. Press the **Delete** button on the top right section.
   ![Database panel](Editing-panel.png)
3. Confirm the deletion. The item will then be removed.

## Modify Database & Table Configuration

To modify a Database or Table configuration,

1. Highlight the database or table which you want to modify.
2. Press the **Configuration** button on the top right section.
   ![Database panel](Editing-panel.png)
   Please notice that configuration button icon for configuring database and table is different:
    * ![Database configuration](Editing-database-configuration-button.png)
    * ![Table configuration](Editing-table-configuration-button.png)
3. Change the database / table configuration
   ![Database root configuration popup](Editing-database-root-configuration-popup.png)
   For root database configuration these fields could be modified
      * **Host**
      * **Port**
      * **Username**
      * **Password**
   ![Database configuration popup](Editing-database-configuration-popup.png)
   For database configuration these fields could be modified
      Charset available:
      * **utf8mb4**
      * **latin1**
      Collation available for **utf8mb4** Charset:
      * **utf8mb4_general_ci**
      * **utf8mb4_unicode_ci**
      Collation available for **latin1** Charset:
      * **latin1_general_ci**
      * **latin1_swedish_ci**
   ![Table configuration popup](Editing-table-configuration-popup.png)
   For table configuration these fields could be modified (Please take note that Engine cannot be changed from **InnoDB** to **MyISAM** after a table has been created and has foreign keys linked to it as **MyISAM** does not support foreign keys)
      Engine available:
      * **InnoDB**
      * **MyISAM**
      Charset available:
      * **utf8mb4**
      * **latin1**
      Collation available for **utf8mb4** Charset:
      * **utf8mb4_general_ci**
      * **utf8mb4_unicode_ci**
      Collation available for **latin1** Charset:
      * **latin1_general_ci**
      * **latin1_swedish_ci**
4. Confirm the configuration change. The item configuration will then be updated.
