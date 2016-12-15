# aac-objects_folded.json

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300312355`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectID_
From column: _data / id_
``` python
return "id/"+getValue("id")
```

#### _objectURL_
From column: _data / link_
``` python
return getValue("link")
```

#### _titleLabel_
From column: _data / title_
``` python
return getValue("title")
```

#### _TitleURI_
From column: _data / ObjectID_
``` python
return "title/id/"+getValue("id")
```

#### _accessionLabel_
From column: _data / accession_number_
``` python
return getValue("accession_number")
```

#### _accessionNumberURI_
From column: _data / TitleURI_
``` python
return "accessionnumber/id/"+getValue("id")
```

#### _creation_place_
From column: _data / Glue_1 / data_creation_city_values_
``` python
c = str(getValue("data_creation_city_values"))
s = str(getValue("data_creation_state_values"))
if c == "" and s == "":
    return ""
elif c == "":
    return s
elif s == "":
    return c
else:
    return c+','+s
```

#### _ProductionURI_
From column: _data / TitleURI_
``` python
return "productionobject/id/"+getValue("id")
```

#### _CreationLocationClassURI_
From column: _data / ProductionURI_
``` python
return "productionobject/creationlocation/id/"+getValue("id")
```

#### _FirstImageURL_
From column: _data / imageconcated_
``` python
url = getValue("imageconcated")
if url == "":
    return url
else:
    return url[:url.index(',')]
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _CreationLocationClassURI_ | `uri` | `crm:E53_Place1`|
| _FirstImageURL_ | `uri` | `crm:E38_Image1`|
| _ObjectID_ | `uri` | `crm:E22_Man-Made_Object1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _accessionLabel_ | `rdfs:label` | `crm:E42_Identifier1`|
| _accessionNumberURI_ | `uri` | `crm:E42_Identifier1`|
| _accession_number_ | `rdf:value` | `crm:E42_Identifier1`|
| _creation_place_ | `rdfs:label` | `crm:E53_Place1`|
| _link_ | `uri` | `foaf:Document1`|
| _objectURL_ | `rdfs:label` | `foaf:Document1`|
| _title_ | `rdf:value` | `crm:E35_Title1`|
| _titleLabel_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `crm:P138i_has_representation` | `crm:E38_Image1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300312355`|
