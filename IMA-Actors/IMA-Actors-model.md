# IMA-SampleActors-Data-for-AAC.csv

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404652`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404662`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404654`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404651`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300379842`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ActorURI_
From column: _ID_
``` python
return "actor/"+getValue("ID")
```

#### _NameURI_
From column: _ActorURI_
``` python
return getValue("ActorURI")+"/name"
```

#### _AppellationValue_
From column: _NAME_FULL_
``` python
return getValue("NAME_FULL")
```

#### _GivenNameURI_
From column: _NAME_FIRST_
``` python
if getValue("NAME_FIRST"):
    return UM.uri_from_fields(getValue("NameURI")+"/given")
else:
    return ""
```

#### _MiddleNameURI_
From column: _NAME_MIDDLE_
``` python
if getValue("NAME_MIDDLE"):
    return UM.uri_from_fields(getValue("NameURI")+"/middle")
else:
    return ""
```

#### _FamilyNameURI_
From column: _NAME_LAST_
``` python
if getValue("NAME_LAST"):
    return UM.uri_from_fields(getValue("NameURI")+"/family")
else:
    return ""
```

#### _NameSuffixURI_
From column: _NAME_SUFFIX_
``` python
if getValue("NAME_SUFFIX"):
    return UM.uri_from_fields(getValue("NameURI")+"/suffix")
else:
    return ""
```

#### _GenderURI_
From column: _SEX_
``` python
if getValue("SEX"):
    return UM.uri_from_fields("thesauri/gender/",getValue("SEX"))
else:
    return ""
```

#### _BirthURI_
From column: _BIRTHDATE_
``` python
if getValue("BIRTHDATE"):
    return getValue("ActorURI")+"/birth"
else:
    return ""
```

#### _DeathURI_
From column: _DEATHDATE_
``` python
if getValue("DEATHDATE"):
    return getValue("ActorURI")+"/death"
else:
    return ""
```

#### _BirthDateURI_
From column: _BirthURI_
``` python
if getValue("BirthURI"):
    return getValue("BirthURI")+"/date"
else:
    return ""
```

#### _DeathDateURI_
From column: _DeathURI_
``` python
if getValue("DeathURI"):
    return getValue("DeathURI")+"/date"
else:
    return ""
```

#### _BirthPlaceURI_
From column: _BIRTHPLACE_
``` python
if getValue("BIRTHPLACE"):
    return UM.uri_from_fields("thesauri/place/",getValue("BIRTHPLACE"))
else:
    return ""
```

#### _DeathPlaceURI_
From column: _DEATHPLACE_
``` python
if getValue("DEATHPLACE"):
    return UM.uri_from_fields("thesauri/place/",getValue("DEATHPLACE"))
else:
    return ""
```

#### _NationalityURI_
From column: _NATIONALITY_
``` python
if getValue("NATIONALITY"):
    return UM.uri_from_fields("thesauri/nationality/",getValue("NATIONALITY"))
else:
    return ""
```

#### _BirthDateEarliest_
From column: _BIRTHDATE_
``` python
b = str(getValue("BIRTHDATE"))
if len(b) == 4:
    return b+"-01-01"
else:
    return ""
```

#### _BirthDateLatest_
From column: _BIRTHDATE_
``` python
b = str(getValue("BIRTHDATE"))
if len(b) == 4:
    return b+"-12-31"
else:
    return ""
```

#### _DeathDateEarliest_
From column: _DEATHDATE_
``` python
b = str(getValue("DEATHDATE"))
if len(b) == 4:
    return b+"-01-01"
else:
    return ""
```

#### _DeathDateLatest_
From column: _DEATHDATE_
``` python
b = str(getValue("DEATHDATE"))
if len(b) == 4:
    return b+"-12-31"
else:
    return ""
```

#### _ActorIDURI_
From column: _ActorURI_
``` python
return "actor/"+getValue("ID")+"/id"
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ActorIDURI_ | `uri` | `crm:E42_Identifier1`|
| _ActorURI_ | `uri` | `crm:E39_Actor1`|
| _AppellationValue_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _BIRTHDATE_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _BIRTHPLACE_ | `rdfs:label` | `crm:E53_Place1`|
| _BirthDateEarliest_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _BirthDateLatest_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _BirthDateURI_ | `uri` | `crm:E52_Time-Span1`|
| _BirthPlaceURI_ | `uri` | `crm:E53_Place1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _DEATHDATE_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _DEATHPLACE_ | `rdfs:label` | `crm:E53_Place2`|
| _DeathDateEarliest_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span2`|
| _DeathDateLatest_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span2`|
| _DeathDateURI_ | `uri` | `crm:E52_Time-Span2`|
| _DeathPlaceURI_ | `uri` | `crm:E53_Place2`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _FamilyNameURI_ | `uri` | `crm:E82_Actor_Appellation4`|
| _GenderURI_ | `uri` | `crm:E55_Type5`|
| _GivenNameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _ID_ | `rdf:value` | `crm:E42_Identifier1`|
| _MiddleNameURI_ | `uri` | `crm:E82_Actor_Appellation3`|
| _NAME_FIRST_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _NAME_FULL_ | `rdfs:label` | `crm:E39_Actor1`|
| _NAME_LAST_ | `rdf:value` | `crm:E82_Actor_Appellation4`|
| _NAME_MIDDLE_ | `rdf:value` | `crm:E82_Actor_Appellation3`|
| _NAME_SUFFIX_ | `rdf:value` | `crm:E82_Actor_Appellation5`|
| _NATIONALITY_ | `rdfs:label` | `crm:E74_Group1`|
| _NameSuffixURI_ | `uri` | `crm:E82_Actor_Appellation5`|
| _NameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _NationalityURI_ | `uri` | `crm:E74_Group1`|
| _SEX_ | `rdfs:label` | `crm:E55_Type5`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E39_Actor1` | `crm:P2_has_type` | `crm:E55_Type5`|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E55_Type1` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404651`|
| `crm:E55_Type2` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404654`|
| `crm:E55_Type3` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404652`|
| `crm:E55_Type4` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404662`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E64_End_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place2`|
| `crm:E74_Group1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300379842`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation2`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation3`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation4`|
| `crm:E82_Actor_Appellation1` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation5`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E82_Actor_Appellation3` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E82_Actor_Appellation4` | `crm:P2_has_type` | `crm:E55_Type3`|
| `crm:E82_Actor_Appellation5` | `crm:P2_has_type` | `crm:E55_Type4`|
