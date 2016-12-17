# aac-objects_folded.json

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300312355`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300080091`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300179869`
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
return getValue("ObjectID")+"/title"
```

#### _accessionLabel_
From column: _data / accession_number_
``` python
return getValue("accession_number")
```

#### _AccessionNumberURI_
From column: _data / TitleURI_
``` python
return getValue("ObjectID")+"/accessionnumber"
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
return getValue("ObjectID")+"/production"
```

#### _CreationLocationClassURI_
From column: _data / ProductionURI_
``` python
return getValue("ObjectID")+"/production/creationlocation"
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

#### _RightsURI_
From column: _data / AccessionNumberURI_
``` python
return getValue("ObjectID")+"/rights"
```

#### _DescriptionValue_
From column: _data / description_
``` python
return getValue("description")
```

#### _DescriptionURI_
From column: _data / RightsURI_
``` python
return getValue("ObjectID")+"/description"
```

#### _ClassificationURI_
From column: _data / DescriptionURI_
``` python
return getValue("ObjectID")+"/type"
```

#### _ClassificationLabelURI_
From column: _data / object_types / TypeURI_
``` python
if getValue('values') != "":
    return getValue('ObjectID')+'/type/'+getValue("values")
else:
    return ""
```

#### _TypeURI_
From column: _data / object_types / TypeURI_
``` python
return getValue('ObjectID')+'/'+getValue("values")
```

#### _MaterialURI_
From column: _data / ClassificationURI_
``` python
return getValue("ObjectID")+"/material"
```

#### _TechniqueURI_
From column: _data / ClassificationURI_
``` python
return getValue("ObjectID")+"/technique"
```

#### _TechniqueLabelURI_
From column: _data / technique_
``` python
if getValue('technique') != "":
    return getValue('ObjectID')+'/technique/'+getValue("technique")
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AccessionNumberURI_ | `uri` | `crm:E42_Identifier1`|
| _ClassificationLabelURI_ | `uri` | `crm:E55_Type1`|
| _ClassificationURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _CreationLocationClassURI_ | `uri` | `crm:E53_Place1`|
| _DescriptionURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _DescriptionValue_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _FirstImageURL_ | `uri` | `crm:E38_Image1`|
| _MaterialURI_ | `uri` | `crm:E57_Material1`|
| _ObjectID_ | `uri` | `crm:E22_Man-Made_Object1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _RightsURI_ | `uri` | `crm:E30_Right1`|
| _TechniqueLabelURI_ | `uri` | `crm:E55_Type2`|
| _TechniqueURI_ | `uri` | `crm:E12_Production2`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _accessionLabel_ | `rdfs:label` | `crm:E42_Identifier1`|
| _accession_number_ | `rdf:value` | `crm:E42_Identifier1`|
| _creation_place_ | `rdfs:label` | `crm:E53_Place1`|
| _description_ | `dc:description` | `crm:E22_Man-Made_Object1`|
| _link_ | `uri` | `foaf:Document1`|
| _objectURL_ | `rdfs:label` | `foaf:Document1`|
| _technique_ | `rdfs:label` | `crm:E55_Type2`|
| _title_ | `rdf:value` | `crm:E35_Title1`|
| _titleLabel_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _values_ | `crm:P3_has_note` | `crm:E30_Right1`|
| _values_ | `rdfs:label` | `crm:E55_Type1`|
| _values_ | `skos:prefLabel` | `crm:E57_Material1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E12_Production2` | `crm:P32_used_general_technique` | `crm:E55_Type2`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E22_Man-Made_Object1` | `crm:P104_is_subject_to` | `crm:E30_Right1`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production2`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E22_Man-Made_Object1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P138i_has_representation` | `crm:E38_Image1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300080091`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300312355`|
| `crm:E55_Type1` | `crm:P21_had_general_purpose` | `xsd:http://vocab.getty.edu/aat/300179869`|
