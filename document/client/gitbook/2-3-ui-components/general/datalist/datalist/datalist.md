# Datalist Component

The 'Datalist' component is used to display data from a given array, list or data sources from connectors.

## Properties

| Property       | Value Sample | Value Type | Description                                                               |
|----------------|--------------|------------|---------------------------------------------------------------------------|
| Name           | dataList1    | string     | Specifies the name or identifier of the Datalist component.               |
| Dataset        | LocalTable1  | string     | Specifies identifier of the dataset containing the tabular data to be displayed.                   |
| Auto Load      | true         | boolean    | If set to true, the Datalist component will automatically load the dataset once. |
| Hide On Print  | false        | boolean    | If set to true, the Datalist component will be hidden when printed.        |
| Style Class    | dataList-style | string   | Specifies the style class to be applied to the Datalist component.        |
| ID Prefix      | dataList_    | string     | [Only used when placed inside a 'Datalist' component] Specifies the prefix used for the unique identification of this component inside a datalist. The name identifier of this component will be overwritten with the concatenation of ID Prefix and ID Field.   |
| ID Field       | data_id | string | [Only used when placed inside a 'Datalist' component] Specifies the field name from a data source bound to the parent 'Datalist' component. The name identifier of this component will be overwritten by concatenating the ID Prefix and the value in the data source referenced by the ID Field. |
| Sortable       | true         | boolean    | If set to true, the Datalist component allows sorting of the table columns. |

## Related Actions

- [loadData](link_to_loadData) - Loads the data from local storage, staging database or 3rd party connector.
- [loadNext](link_to_loadNext) - Loads the following next records of the table or dataset.

## Example Uses

![Example Use 1](path/to/screenshot1.png)
_Description or caption for example use 1._

![Example Use 2](path/to/screenshot2.png)
_Description or caption for example use 2._

![Example Use 3](path/to/screenshot3.png)
_Description or caption for example use 3._

...
