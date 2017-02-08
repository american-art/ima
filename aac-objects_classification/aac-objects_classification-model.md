# aac-objects_folded_jsonlines.json

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300179869`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _data / id_
``` python
return "object/id/"+getValue("id")
```

#### _ClassificationURI_
From column: _data / number_of_parts_
``` python
return getValue("ObjectURI")+"/classification"
```

#### _TypeURI_
From column: _data / object_types / values_
``` python
return UM.uri_from_fields("thesauri/classification/",getValue("values"))
```


## Selections
#### _DEFAULT_TEST_
From column: _data / date_accession_
<br>Operation: `Union`
``` python
return "Visual Works:" not in getValue("record_type")
```


## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ClassificationURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _TypeURI_ | `uri` | `crm:E55_Type1`|
| _values_ | `rdfs:label` | `crm:E55_Type1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `xsd:http://vocab.getty.edu/aat/300179869`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type1`|
