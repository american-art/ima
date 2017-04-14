# aac-objects_folded_jsonlines.json

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

#### Literal Node: `http://vocab.getty.edu/aat/300026687`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300263534`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300266036`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/ulan/500300517`
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
return "object/"+getValue("id")
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
    return c+', '+s
```

#### _ProductionURI_
From column: _data / TitleURI_
``` python
return getValue("ObjectID")+"/production"
```

#### _NIU2_
From column: _data / ProductionURI_
``` python

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

#### _NIU1_
From column: _data / AccessionNumberURI_
``` python

```

#### _DescriptionValue_
From column: _data / description_
``` python
return getValue("description")
```

#### _DescriptionURI_
From column: _data / NIU1_
``` python
if getValue("description"):
    return getValue("ObjectID")+"/description"
else:
    return ""
```

#### _ClassificationURI_
From column: _data / DescriptionURI_
``` python
if "Visual Works:" in getValue("record_type"):
    return getValue("ObjectID")+"/type"
else:
    return ""
```

#### _ClassificationLabelURI_
From column: _data / object_types / values_
``` python
if getValue('values') != "":
    return UM.uri_from_fields(getValue('ObjectID')+'/type/', getValue("values"))
else:
    return ""
```

#### _NotInUse_
From column: _data / ClassificationURI_
``` python

```

#### _TechniqueURI_
From column: _data / ClassificationURI_
``` python
return getValue("ProductionURI")
```

#### _TechniqueLabelURI_
From column: _data / technique_
``` python
if getValue('technique') != "":
    return UM.uri_from_fields('thesauri/technique/',getValue("technique"))
else:
    return ""
```

#### _CreditLineURI_
From column: _data / TechniqueLabelURI_
``` python
return getValue('ObjectID')+'/creditline'
```

#### _CollectionURI_
From column: _data / CreditLineURI_
``` python

```

#### _DepartmentURI_
From column: _data / CollectionURI_
``` python

```

#### _InformationObjectURI_
From column: _data / DepartmentURI_
``` python

```

#### _ConceptURI_
From column: _data / InformationObjectURI_
``` python

```

#### _CreationDateURI_
From column: _data / ObjectID_
``` python
return getValue("ProductionURI")
```

#### _CreationDateTimeSpanURI_
From column: _data / CreationDateURI_
``` python
return getValue("ProductionURI")+'/timespan'
```

#### _CreatorURI_
From column: _data / actors / id_
``` python
return 'actor/'+getValue("id")
```

#### _ProductionCreatorURI_
From column: _data / ConceptURI_
``` python
return getValue('ProductionURI')
```

#### _DimensionDepthURI_
From column: _data / dimensions / PhyType_tab_
``` python
if getValue("PhyDepth_tab"):
    return UM.uri_from_fields(getValue("ObjectID")+'/depth/',getValue('PhyType_tab'))
else:
    return ""
```

#### _DimensionDiameterURI_
From column: _data / dimensions / PhyType_tab_
``` python
if getValue("PhyDiameter_tab"):
    return UM.uri_from_fields(getValue("ObjectID")+'/diameter/',getValue('PhyType_tab'))
else:
    return ""
```

#### _DimensionHeightURI_
From column: _data / dimensions / PhyType_tab_
``` python
if getValue("PhyHeight_tab"):
    return UM.uri_from_fields(getValue("ObjectID")+'/height/',getValue('PhyType_tab'))
else:
    return ""
```

#### _DimensionWidthURI_
From column: _data / dimensions / PhyType_tab_
``` python
if getValue("PhyWidth_tab"):
    return UM.uri_from_fields(getValue("ObjectID")+'/width/',getValue('PhyType_tab'))
else:
    return ""
```

#### _DimensionDepthUnit_
From column: _data / dimensions / PhyUnitLength_tab_
``` python
v = getValue("PhyUnitLength_tab").replace('.','')
if "." in v and getValue("DimensionDepthURI"):
    v = v.replace('.','').strip().lower()
return v
```

#### _DimensionWidthUnit_
From column: _data / dimensions / DimensionDepthUnit_
``` python
v = getValue("PhyUnitLength_tab").replace('.','')
if "." in v:
    v = v.replace('.','').strip().lower()
return v
```

#### _DimensionHeightUnit_
From column: _data / dimensions / DimensionWidthUnit_
``` python
v = getValue("PhyUnitLength_tab").replace('.','')
if "." in v:
    v = v.replace('.','').strip().lower()
return v
```

#### _DimensionDiameterUnit_
From column: _data / dimensions / DimensionHeightUnit_
``` python
v = getValue("PhyUnitLength_tab").replace('.','')
if "." in v:
    v = v.replace('.','').strip().lower()
return v
```

#### _DimensionsTextURI_
From column: _data / dimensions / DimensionWidthURI_
``` python
if "Metric" in getValue("PhyDimensionNotes_tab"):
    return getValue("ObjectID")+'/dimensiontext'
else:
    return ""
```

#### _OwnerURI_
From column: _data / ObjectID_
``` python
return "http://data.americanartcollaborative.org/ima"
```

#### _OwnerLabel_
From column: _data / OwnerURI_
``` python
return "Indianapolis Museum of Art"
```

#### _DeptURI_
From column: _data / department / values_
``` python
return UM.uri_from_fields("thesauri/department/",getValue("values"))
```

#### _PrefID_Label_
From column: _data / id_
``` python
return getValue("id")
```

#### _PrefID_URI_
From column: _data / PrefID_Label_
``` python
return getValue("ObjectID")+"/id"
```

#### _PhysicalObjectURI_
From column: _data / department / values_
``` python
if getValue("values"):
    return UM.uri_from_fields("thesauri/collection/",getValue("values"))
else:
    return ""
```

#### _MaterialURI1_
From column: _data / mediums / values_
``` python
if getValue("values"):
    return UM.uri_from_fields("thesauri/material/",getValue("values"))
else:
    return ""
```

#### _RightsURI_
From column: _data / rights / values_
``` python
if getValue("values"): 
    return getValue("ObjectID")+"/rights"
else:
    return ""
```

#### _StartDateFormatted_
From column: _data / date_earliest_
``` python
return getValue("date_earliest")+"-01-01"
```

#### _EndDateFormatted_
From column: _data / date_latest_
``` python
return getValue("date_latest")+"-12-31"
```

#### _DateLabel_
From column: _data / CreationDateTimeSpanURI_
``` python
return getValue("StartDateFormatted") + " to " + getValue("EndDateFormatted")
```

#### _DepthUnitURI_
From column: _data / dimensions / PhyDepth_tab_
``` python
if getValue("DimensionDepthUnit") and getValue("DimensionDepthURI"):
    return UM.uri_from_fields("thesauri/dimension_type/",getValue("DimensionDepthUnit"))
else:
    return ""
```

#### _DiameterUnitURI_
From column: _data / dimensions / PhyDiameter_tab_
``` python
if getValue("DimensionDiameterUnit") and getValue("DimensionDiameterURI"):
    return UM.uri_from_fields("thesauri/dimension_type/",getValue("DimensionDiameterUnit"))
else:
    return ""
```

#### _PhyHeight_tab_
From column: _data / dimensions / PhyHeight_tab_
``` python
return getValue("PhyHeight_tab")
```

#### _HeightUnitURI_
From column: _data / dimensions / PhyHeight_tab_
``` python
if getValue("DimensionHeightUnit") and getValue("DimensionHeightURI"):
    return UM.uri_from_fields("thesauri/dimension_type/",getValue("DimensionHeightUnit"))
else:
    return ""
```

#### _WidthUnitURI_
From column: _data / dimensions / PhyWidth_tab_
``` python
if getValue("DimensionWidthUnit") and getValue("DimensionWidthURI"):
    return UM.uri_from_fields("thesauri/dimension_type/",getValue("DimensionWidthUnit"))
else:
    return ""
```

#### _PlaceURI_
From column: _data / Glue_1 / creation_place_
``` python
if getValue("creation_place"):
    return UM.uri_from_fields("thesauri/place/",getValue("creation_place"))
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
| _CreationDateTimeSpanURI_ | `uri` | `crm:E52_Time-Span1`|
| _CreationDateURI_ | `uri` | `crm:E12_Production3`|
| _CreatorURI_ | `uri` | `crm:E39_Actor1`|
| _CreditLineURI_ | `uri` | `crm:E33_Linguistic_Object2`|
| _DeptURI_ | `uri` | `crm:E74_Group1`|
| _DepthUnitURI_ | `uri` | `crm:E58_Measurement_Unit1`|
| _DescriptionURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _DescriptionValue_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _DiameterUnitURI_ | `uri` | `crm:E58_Measurement_Unit2`|
| _DimensionDepthURI_ | `uri` | `crm:E54_Dimension4`|
| _DimensionDiameterURI_ | `uri` | `crm:E54_Dimension3`|
| _DimensionDiameterUnit_ | `rdf:value` | `crm:E58_Measurement_Unit2`|
| _DimensionHeightURI_ | `uri` | `crm:E54_Dimension2`|
| _DimensionHeightUnit_ | `rdf:value` | `crm:E58_Measurement_Unit3`|
| _DimensionWidthURI_ | `uri` | `crm:E54_Dimension1`|
| _DimensionWidthUnit_ | `rdf:value` | `crm:E58_Measurement_Unit4`|
| _DimensionsTextURI_ | `uri` | `crm:E33_Linguistic_Object3`|
| _EndDateFormatted_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _FirstImageURL_ | `uri` | `crm:E38_Image1`|
| _HeightUnitURI_ | `uri` | `crm:E58_Measurement_Unit3`|
| _MaterialURI1_ | `uri` | `crm:E57_Material1`|
| _ObjectID_ | `uri` | `crm:E22_Man-Made_Object1`|
| _OwnerLabel_ | `rdfs:label` | `crm:E40_Legal_Body1`|
| _OwnerURI_ | `uri` | `crm:E40_Legal_Body1`|
| _PhyDepth_tab_ | `rdf:value` | `crm:E54_Dimension4`|
| _PhyDiameter_tab_ | `rdf:value` | `crm:E54_Dimension3`|
| _PhyDimensionNotes_tab_ | `rdf:value` | `crm:E33_Linguistic_Object3`|
| _PhyHeight_tab_ | `rdf:value` | `crm:E54_Dimension2`|
| _PhyWidth_tab_ | `rdf:value` | `crm:E54_Dimension1`|
| _PhysicalObjectURI_ | `uri` | `crm:E19_Physical_Object1`|
| _PlaceURI_ | `uri` | `crm:E53_Place1`|
| _PrefID_Label_ | `rdfs:label` | `crm:E42_Identifier2`|
| _PrefID_URI_ | `uri` | `crm:E42_Identifier2`|
| _ProductionCreatorURI_ | `uri` | `crm:E12_Production4`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _RightsURI_ | `uri` | `crm:E30_Right1`|
| _StartDateFormatted_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _TechniqueLabelURI_ | `uri` | `crm:E55_Type2`|
| _TechniqueURI_ | `uri` | `crm:E12_Production2`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _WidthUnitURI_ | `uri` | `crm:E58_Measurement_Unit4`|
| _accessionLabel_ | `rdfs:label` | `crm:E42_Identifier1`|
| _accession_number_ | `rdf:value` | `crm:E42_Identifier1`|
| _creation_place_ | `rdfs:label` | `crm:E53_Place1`|
| _credit_line_ | `rdf:value` | `crm:E33_Linguistic_Object2`|
| _date_earliest_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _description_ | `dc:description` | `crm:E22_Man-Made_Object1`|
| _id_ | `rdf:value` | `crm:E42_Identifier2`|
| _link_ | `uri` | `foaf:Document1`|
| _objectURL_ | `rdfs:label` | `foaf:Document1`|
| _technique_ | `rdfs:label` | `crm:E55_Type2`|
| _title_ | `rdf:value` | `crm:E35_Title1`|
| _titleLabel_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _values_ | `rdfs:label` | `crm:E55_Type1`|
| _values_ | `crm:P3_has_note` | `crm:E30_Right1`|
| _values_ | `skos:prefLabel` | `crm:E57_Material1`|
| _values_ | `rdfs:label` | `crm:E74_Group1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E12_Production2` | `crm:P32_used_general_technique` | `crm:E55_Type2`|
| `crm:E12_Production3` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E12_Production4` | `crm:P14_carried_out_by` | `crm:E39_Actor1`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `http://vocab.getty.edu/aat/300179869`|
| `crm:E19_Physical_Object1` | `crm:P49_has_former_or_current_keeper` | `crm:E74_Group1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production2`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production3`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production4`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P46i_forms_part_of` | `crm:E19_Physical_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P104_is_subject_to` | `crm:E30_Right1`|
| `crm:E22_Man-Made_Object1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object2`|
| `crm:E22_Man-Made_Object1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object3`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P138i_has_representation` | `crm:E38_Image1`|
| `crm:E22_Man-Made_Object1` | `crm:P52_has_current_owner` | `crm:E40_Legal_Body1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier2`|
| `crm:E22_Man-Made_Object1` | `crm:P43_has_dimension` | `crm:E54_Dimension1`|
| `crm:E22_Man-Made_Object1` | `crm:P43_has_dimension` | `crm:E54_Dimension2`|
| `crm:E22_Man-Made_Object1` | `crm:P43_has_dimension` | `crm:E54_Dimension3`|
| `crm:E22_Man-Made_Object1` | `crm:P43_has_dimension` | `crm:E54_Dimension4`|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object3`|
| `crm:E22_Man-Made_Object1` | `crm:P129i_is_subject_of` | `crm:E33_Linguistic_Object2`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300080091`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300026687`|
| `crm:E33_Linguistic_Object3` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300266036`|
| `crm:E35_Title1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E40_Legal_Body1` | `skos:exactMatch` | `http://vocab.getty.edu/ulan/500300517`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300312355`|
| `crm:E42_Identifier2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E54_Dimension1` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit4`|
| `crm:E54_Dimension2` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit3`|
| `crm:E54_Dimension3` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit2`|
| `crm:E54_Dimension4` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
| `crm:E74_Group1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300263534`|
