# IMA-SampleObjects-Data-for-AAC.csv

## Add Column
#### _OwnerURI_
From column: _ID_
<br/>Value: `http://data.americanartcollaborative.org/ima`

#### _OwnerLabel_
From column: _OwnerURI_
<br/>Value: `Indianapolis Museum of Art`


## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/ulan/500300517`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300312355`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300080091`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300026687`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300266036`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300179869`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300263534`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _ID_
``` python
return "object/"+getValue("ID")
```

#### _AccessionNumberURI_
From column: _ACCESSION_NUMBER_
``` python
return getValue("ObjectURI")+"/accessionnumber"
```

#### _idURI_
From column: _ID_
``` python
return getValue("ObjectURI")+"/id"
```

#### _TitleLabel_
From column: _TITLE_
``` python
return getValue("TITLE")
```

#### _TitleURI_
From column: _TITLE_
``` python
if getValue("TITLE"):
    return getValue("ObjectURI")+"/title"
else:
    return ""
```

#### _TypeURI_
From column: _OBJECT_TYPES_SPLIT / Values_
``` python
if getValue("Values"):
    return UM.uri_from_fields("thesauri/type/",getValue("Values"))
else:
    return ""
```

#### _ClassificationURI_
From column: _OBJECT_TYPES_
``` python
if getValue("OBJECT_TYPES"):
    return getValue("ObjectURI")+"/typeassignment"
else:
    return ""
```

#### _ProductionURI_
From column: _DATE_CREATED_
``` python
return getValue("ObjectURI")+"/production"
```

#### _CreationTimeSpanURI_
From column: _ProductionURI_
``` python
if getValue("DATE_CREATED"):
    return getValue("ObjectURI")+"/production/timespan"
else:
    return ""
```

#### _StartDateFormatted_
From column: _DATE_EARLIEST_
``` python
s = str(getValue("DATE_EARLIEST"))
if len(s) == 4:
    return s+"-01-01"
else:
    return ""
```

#### _EndDateFormatted_
From column: _DATE_LATEST_
``` python
e = str(getValue("DATE_EARLIEST"))
if len(e) == 4:
    return e+"-12-31"
else:
    return ""
```

#### _DescriptionURI_
From column: _DESCRIPTION_
``` python
if getValue("DESCRIPTION"):
    return getValue("ObjectURI")+"/description"
else:
    return ""
```

#### _CreditLineURI_
From column: _CREDIT_LINE_
``` python
if getValue("CREDIT_LINE"):
    return getValue("ObjectURI")+"/creditline"
else:
    return ""
```

#### _MaterialURI_
From column: _MEDIUMS_SPLIT / Values_
``` python
if getValue("Values"):
    return UM.uri_from_fields("thesauri/material/",getValue("Values"))
else:
    return ""
```

#### _CollectionURI_
From column: _Collection_Name_
``` python
return UM.uri_from_fields("thesauri/collection/",getValue("Collection_Name"))
```

#### _ActorURI_
From column: _ACTORS_SPLIT / Values_
``` python
if getValue("Values"):
    return UM.uri_from_fields("actor/",getValue("Values"))
else:
    return ""
```

#### _DimensionsTextURI_
From column: _CONVERTED_DIMENSIONS_
``` python
if getValue("CONVERTED_DIMENSIONS"):
    return getValue("ObjectURI")+"/dimensionstext"
else:
    return ""
```

#### _RightsURI_
From column: _RIGHTS_
``` python
if getValue("RIGHTS"):
    return getValue("ObjectURI")+"/rights"
else:
    return ""
```

#### _TechniqueURI_
From column: _TECHNIQUE_SPLIT / Values_
``` python
if getValue("Values"):
    return UM.uri_from_fields("thesauri/technique/",getValue("Values"))
else:
    return ""
```

#### _AcquisitionURI_
From column: _DATE_ACCESSION_
``` python
if getValue("DATE_ACCESSION"):
    return getValue("ObjectURI")+"/acquisition"
else:
    return ""
```

#### _AcquisitionTimeSpanURI_
From column: _AcquisitionURI_
``` python
if getValue("DATE_ACCESSION"):
    return getValue("ObjectURI")+"/acquisitiontimespan"
else:
    return ""
```

#### _DepartmentURI_
From column: _PhysicalObjectURI_
``` python
return "thesauri/curatorialdepartment"
```

#### _DepartmentName_
From column: _DepartmentURI_
``` python
return "Indianapolis Museum of Art Curatorial Department"
```

#### _LinkURI_
From column: _LINK_
``` python
return getValue("LINK")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ACCESSION_NUMBER_ | `rdf:value` | `crm:E42_Identifier1`|
| _AccessionNumberURI_ | `uri` | `crm:E42_Identifier1`|
| _AcquisitionTimeSpanURI_ | `uri` | `crm:E52_Time-Span2`|
| _AcquisitionURI_ | `uri` | `crm:E8_Acquisition1`|
| _ActorURI_ | `uri` | `crm:E39_Actor1`|
| _CONVERTED_DIMENSIONS_ | `rdf:value` | `crm:E33_Linguistic_Object3`|
| _CREDIT_LINE_ | `rdf:value` | `crm:E33_Linguistic_Object2`|
| _ClassificationURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _CollectionURI_ | `uri` | `crm:E19_Physical_Object1`|
| _Collection_Name_ | `rdfs:label` | `crm:E19_Physical_Object1`|
| _CreationTimeSpanURI_ | `uri` | `crm:E52_Time-Span1`|
| _CreditLineURI_ | `uri` | `crm:E33_Linguistic_Object2`|
| _DATE_ACCESSION_ | `crm:P3_has_note` | `crm:E52_Time-Span2`|
| _DATE_CREATED_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _DESCRIPTION_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _DepartmentName_ | `rdfs:label` | `crm:E74_Group1`|
| _DepartmentURI_ | `uri` | `crm:E74_Group1`|
| _DescriptionURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _DimensionsTextURI_ | `uri` | `crm:E33_Linguistic_Object3`|
| _EndDateFormatted_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _ID_ | `rdf:value` | `crm:E42_Identifier2`|
| _IMAGEURL_ | `uri` | `crm:E38_Image1`|
| _LINK_ | `rdfs:label` | `crm:E31_Document1`|
| _LinkURI_ | `uri` | `crm:E31_Document1`|
| _MaterialURI_ | `uri` | `crm:E57_Material1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _OwnerLabel_ | `rdfs:label` | `crm:E40_Legal_Body1`|
| _OwnerURI_ | `uri` | `crm:E40_Legal_Body1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _RIGHTS_ | `crm:P3_has_note` | `crm:E30_Right1`|
| _RightsURI_ | `uri` | `crm:E30_Right1`|
| _StartDateFormatted_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _TITLE_ | `rdf:value` | `crm:E35_Title1`|
| _TechniqueURI_ | `uri` | `crm:E55_Type2`|
| _TitleLabel_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _TypeURI_ | `uri` | `crm:E55_Type1`|
| _Values_ | `rdfs:label` | `crm:E55_Type1`|
| _Values_ | `skos:prefLabel` | `crm:E57_Material1`|
| _Values_ | `rdfs:label` | `crm:E55_Type2`|
| _idURI_ | `uri` | `crm:E42_Identifier2`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor1`|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E12_Production1` | `crm:P32_used_general_technique` | `crm:E55_Type2`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `http://vocab.getty.edu/aat/300179869`|
| `crm:E19_Physical_Object1` | `crm:P49_has_former_or_current_keeper` | `crm:E74_Group1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P46i_forms_part_of` | `crm:E19_Physical_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P104_is_subject_to` | `crm:E30_Right1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `crm:E31_Document1`|
| `crm:E22_Man-Made_Object1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object2`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object3`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P138i_has_representation` | `crm:E38_Image1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier2`|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material1`|
| `crm:E22_Man-Made_Object1` | `crm:P24i_changed_ownership_through` | `crm:E8_Acquisition1`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E22_Man-Made_Object1` | `crm:P52_has_current_owner` | `crm:E40_Legal_Body1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300080091`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300026687`|
| `crm:E33_Linguistic_Object3` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300266036`|
| `crm:E35_Title1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E40_Legal_Body1` | `skos:exactMatch` | `http://vocab.getty.edu/ulan/500300517`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300312355`|
| `crm:E42_Identifier2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E74_Group1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300263534`|
| `crm:E8_Acquisition1` | `crm:P22_transferred_title_to` | `crm:E40_Legal_Body1`|
| `crm:E8_Acquisition1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
