# IMA-SampleObjects-Dimensions-Data-for-AAC.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300266036`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300055647`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300055644`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300055624`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300072633`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _OBJECTID_
``` python
return "object/"+getValue("OBJECTID")
```

#### _DimensionUnitURI_
From column: _LENGTHUNIT_
``` python
return "thesauri/dimensionunit/"+getValue("LENGTHUNIT")
```

#### _DimensionHeightURI_
From column: _HEIGHT_
``` python
if getValue("HEIGHT"):
    return UM.uri_from_fields(getValue("ObjectURI")+"/",getValue("DIMTYPE"))+"/height"
else:
    return ""
```

#### _DimensionWidthURI_
From column: _WIDTH_
``` python
if getValue("WIDTH"):
    return UM.uri_from_fields(getValue("ObjectURI")+"/",getValue("DIMTYPE"))+"/width"
else:
    return ""
```

#### _DimensionDepthURI_
From column: _DEPTH_
``` python
if getValue("DEPTH"):
    return UM.uri_from_fields(getValue("ObjectURI")+"/",getValue("DIMTYPE"))+"/depth"
else:
    return ""
```

#### _DimensionDiameterURI_
From column: _DIAMETER_
``` python
if getValue("DIAMETER"):
    return UM.uri_from_fields(getValue("ObjectURI")+"/",getValue("DIMTYPE"))+"/diameter"
else:
    return ""
```

#### _DimensionNoteURI_
From column: _NOTES_
``` python
if getValue("NOTES"):
    return UM.uri_from_fields(getValue("ObjectURI")+"/",getValue("DIMTYPE"))+"/note"
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _DEPTH_ | `rdf:value` | `crm:E54_Dimension3`|
| _DIAMETER_ | `rdf:value` | `crm:E54_Dimension4`|
| _DimensionDepthURI_ | `uri` | `crm:E54_Dimension3`|
| _DimensionDiameterURI_ | `uri` | `crm:E54_Dimension4`|
| _DimensionHeightURI_ | `uri` | `crm:E54_Dimension1`|
| _DimensionNoteURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _DimensionUnitURI_ | `uri` | `crm:E58_Measurement_Unit1`|
| _DimensionWidthURI_ | `uri` | `crm:E54_Dimension2`|
| _HEIGHT_ | `rdf:value` | `crm:E54_Dimension1`|
| _LENGTHUNIT_ | `rdfs:label` | `crm:E58_Measurement_Unit1`|
| _NOTES_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _WIDTH_ | `rdf:value` | `crm:E54_Dimension2`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P43_has_dimension` | `crm:E54_Dimension1`|
| `crm:E22_Man-Made_Object1` | `crm:P43_has_dimension` | `crm:E54_Dimension2`|
| `crm:E22_Man-Made_Object1` | `crm:P43_has_dimension` | `crm:E54_Dimension3`|
| `crm:E22_Man-Made_Object1` | `crm:P43_has_dimension` | `crm:E54_Dimension4`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300266036`|
| `crm:E54_Dimension1` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
| `crm:E54_Dimension1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055644`|
| `crm:E54_Dimension2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055647`|
| `crm:E54_Dimension2` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
| `crm:E54_Dimension3` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300072633`|
| `crm:E54_Dimension3` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
| `crm:E54_Dimension4` | `crm:P91_has_unit` | `crm:E58_Measurement_Unit1`|
| `crm:E54_Dimension4` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055624`|
