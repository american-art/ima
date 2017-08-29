# IMA-SampleObjects-Creation-Location-Data-for-AAC.csv

## Add Column

## Add Node/Literal

## PyTransforms
#### _ObjectURI_
From column: _OBJECTID_
``` python
return "object/"+getValue("OBJECTID")
```

#### _ProductionURI_
From column: _ObjectURI_
``` python
return "object/"+getValue("OBJECTID")+"/production"
```

#### _CreationPlaceLabel_
From column: _CITY_
``` python
c = str(getValue("CITY"))
s = str(getValue("STATE"))
if c == "" and s == "":
    return ""
elif c == "":
    return s
elif s == "":
    return c
else:
    return c+', '+s
```

#### _CreationPlaceURI_
From column: _CreationPlaceLabel_
``` python
if getValue("CreationPlaceLabel"):
    return UM.uri_from_fields("thesauri/place/",getValue("CreationPlaceLabel"))
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _CreationPlaceLabel_ | `rdfs:label` | `crm:E53_Place1`|
| _CreationPlaceURI_ | `uri` | `crm:E53_Place1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
