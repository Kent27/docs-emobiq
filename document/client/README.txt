# document

Include that ERP tables are driven by a connector, user can directly use
loadData. ERP tables are not cached.

local table and sqlite table are the only tables that have memory. Using
loadTable helps to retrieve updated table. 

May make more sense that Datalist refreshes if insert data or other
relevant services are called
