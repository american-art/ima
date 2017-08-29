# IMA-Technique-AAT-Data.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _TechniqueURI_
From column: _TECHNIQUE_
``` python
return UM.uri_from_fields("thesauri/technique/",getValue("TECHNIQUE"))
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AAT Term_ | `rdfs:label` | `crm:E55_Type2`|
| _AAT URI_ | `uri` | `crm:E55_Type2`|
| _TECHNIQUE_ | `rdfs:label` | `crm:E55_Type1`|
| _TechniqueURI_ | `uri` | `crm:E55_Type1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E55_Type1` | `skos:broadMatch` | `crm:E55_Type2`|
| `crm:E55_Type2` | `skos:inScheme` | `http://vocab.getty.edu/aat/`|
