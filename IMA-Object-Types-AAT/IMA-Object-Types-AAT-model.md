# IMA-Object-Types-AAT-Data.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectTypesURI_
From column: _OBJECT_TYPES_
``` python
return UM.uri_from_fields("thesauri/type/",getValue("OBJECT_TYPES"))
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AAT Term_ | `rdfs:label` | `crm:E55_Type2`|
| _AAT URI_ | `uri` | `crm:E55_Type2`|
| _OBJECT_TYPES_ | `rdfs:label` | `crm:E55_Type1`|
| _ObjectTypesURI_ | `uri` | `crm:E55_Type1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E55_Type1` | `skos:broadMatch` | `crm:E55_Type2`|
| `crm:E55_Type2` | `skos:inScheme` | `http://vocab.getty.edu/aat/`|
