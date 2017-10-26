# IMA-Objects-Dimensions-Data.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300055644`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300055647`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300072633`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300055624`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300266036`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _OBJECTID_
``` python
return "object/"+getValue("OBJECTID")
```

#### _PartURI_
From column: _DIMTYPE_
``` python
if getValue("DIMTYPE"):
    return UM.uri_from_fields(getValue("ObjectURI")+"/",getValue("DIMTYPE"))
else:
    return ""
```

#### _DimensionHeightURI_
From column: _HEIGHT_
``` python
if getValue("HEIGHT"):
    return getValue("PartURI")+"/dimension/height"
else:
    return ""
```

#### _DimensionWidthURI_
From column: _WIDTH_
``` python
if getValue("WIDTH"):
    return getValue("PartURI")+"/dimension/width"
else:
    return ""
```

#### _DimensionDepthURI_
From column: _DEPTH_
``` python
if getValue("DEPTH"):
    return getValue("PartURI")+"/dimension/depth"
else:
    return ""
```

#### _DimensionDiameterURI_
From column: _DIAMETER_
``` python
if getValue("DIAMETER"):
    return getValue("PartURI")+"/dimension/diameter"
else:
    return ""
```

#### _DimensionWeightURI_
From column: _WEIGHT_
``` python
if getValue("WEIGHT"):
    return getValue("PartURI")+"/dimension/weight"
else:
    return ""
```

#### _DimensionUnitURI_
From column: _LENGTHUNIT_
``` python
if getValue("LENGTHUNIT"):
    return UM.uri_from_fields("/thesauri/dimensionunit/",getValue("LENGTHUNIT"))
else:
    return ""
```

#### _WeightUnitURI_
From column: _WEIGHTUNIT_
``` python
if getValue("WEIGHTUNIT"):
    return UM.uri_from_fields("/thesauri/dimensionunit/",getValue("WEIGHTUNIT"))
else:
    return ""
```

#### _DimensionNoteURI_
From column: _NOTES_
``` python
if getValue("NOTES"):
    return getValue("PartURI")+"/dimension/note"
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _DEPTH_ | `rdf:value` | `crm:E54_Dimension3`|
| _DIAMETER_ | `rdf:value` | `crm:E54_Dimension4`|
| _DIMTYPE_ | `rdfs:label` | `crm:E18_Physical_Thing1`|
| _DimensionDepthURI_ | `uri` | `crm:E54_Dimension3`|
| _DimensionDiameterURI_ | `uri` | `crm:E54_Dimension4`|
| _DimensionHeightURI_ | `uri` | `crm:E54_Dimension1`|
| _DimensionNoteURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _DimensionUnitURI_ | `uri` | `crm:E58_Measurement_Unit1`|
| _DimensionWeightURI_ | `uri` | `crm:E54_Dimension5`|
| _DimensionWidthURI_ | `uri` | `crm:E54_Dimension2`|
| _HEIGHT_ | `rdf:value` | `crm:E54_Dimension1`|
| _LENGTHUNIT_ | `rdfs:label` | `crm:E58_Measurement_Unit1`|
| _NOTES_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _PartURI_ | `uri` | `crm:E18_Physical_Thing1`|
| _WEIGHT_ | `rdf:value` | `crm:E54_Dimension5`|
| _WEIGHTUNIT_ | `rdfs:label` | `crm:E58_Measurement_Unit2`|
| _WIDTH_ | `rdf:value` | `crm:E54_Dimension2`|
| _WeightUnitURI_ | `uri` | `crm:E58_Measurement_Unit2`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E18_Physical_Thing1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E18_Physical_Thing1` | `crm:P43_has_dimension` | `crm:E54_Dimension1`|
| `crm:E18_Physical_Thing1` | `crm:P43_has_dimension` | `crm:E54_Dimension2`|
| `crm:E18_Physical_Thing1` | `crm:P43_has_dimension` | `crm:E54_Dimension3`|
| `crm:E18_Physical_Thing1` | `crm:P43_has_dimension` | `crm:E54_Dimension4`|
| `crm:E18_Physical_Thing1` | `crm:P43_has_dimension` | `crm:E54_Dimension5`|
| `crm:E22_Man-Made_Object1` | `crm:P46_is_composed_of` | `crm:E18_Physical_Thing1`|
| `crm:E54_Dimension1` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
| `crm:E54_Dimension1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055644`|
| `crm:E54_Dimension2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055647`|
| `crm:E54_Dimension2` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
| `crm:E54_Dimension3` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300072633`|
| `crm:E54_Dimension3` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
| `crm:E54_Dimension4` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
| `crm:E54_Dimension4` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055624`|
| `crm:E54_Dimension5` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit2`|
| `crm:E54_Dimension5` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300266036`|
