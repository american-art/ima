# aac-actors.json

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404651`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404654`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404652`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404662`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300055147`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300379842`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/ulan`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _fullnamelabel_
From column: _data / name_full_
``` python
return getValue("name_full")
```

#### _firstid_
From column: _data / id_concatenated_
``` python
if ';' not in getValue("id_concatenated"): 
    return getValue("id_concatenated")
else:
    return getValue("id_concatenated")[:getValue("id_concatenated").index(';')]
```

#### _uri_
From column: _data / firstid_
``` python
if getValue("name_full")!="Unknown":
    return "actor/"+getValue('firstid')
else:
    ""
```

#### _NameURI_
From column: _data / uri_
``` python
if getValue("name_full") and getValue("name_full")!="Unknown":
    return getValue('uri')+"/name"
else:
    return ""
```

#### _GivenNameClassURI_
From column: _data / NameURI_
``` python
if getValue("name_first"):
    return getValue('uri')+"/name/first_name"
else:
    return ""
```

#### _GivenNameTypeClass_
From column: _data / GivenNameClassURI_
``` python
return getValue('uri')+"/name/givenname/type"
```

#### _MiddleNameClassURI_
From column: _data / GivenNameClassURI_
``` python
if getValue("name_middle"):
    return getValue('uri')+"/name/middle_name"
else:
    return ""
```

#### _MiddleNameTypeClassURI_
From column: _data / MiddleNameClassURI_
``` python
return getValue('uri')+"/name/middlename/type"
```

#### _FamilyNameClassURI_
From column: _data / GivenNameClassURI_
``` python
if getValue("name_last") and getValue("name_last")!="Unknown":
    return getValue('uri')+"/name/last_name"
else:
    return ""
```

#### _FamilyNameTypeClassURI_
From column: _data / FamilyNameClassURI_
``` python
return getValue('uri')+"/name/familyname/type"
```

#### _NameSuffixClassURI_
From column: _data / MiddleNameClassURI_
``` python
if getValue("name_suffix"):
    return getValue('uri')+"/name/suffix"
else:
    return ""
```

#### _NameSuffixTypeClassURI_
From column: _data / NameSuffixClassURI_
``` python
return getValue('uri')+"/name/suffix/type"
```

#### _GenderClassURI_
From column: _data / NameSuffixClassURI_
``` python
if getValue("sex"):
    return UM.uri_from_fields("thesauri/gender/", getValue("sex"))
else:
    return ""
```

#### _GenderTypeClassURI_
From column: _data / GenderClassURI_
``` python
if getValue("sex"):
    return getValue('uri')+"/gender/type"
else:
    return ""
```

#### _birthdatelabel_
From column: _data / dates / birth_
``` python
if getValue("birth"):
    return getValue("birth")
else:
    return ""
```

#### _deathdatelabel_
From column: _data / dates / death_
``` python
return getValue("death")
```

#### _BirthURI_
From column: _data / dates / birth_
``` python
if getValue("birth"):
    return getValue('uri')+"/birth"
else:
    return ""
```

#### _BirthDateURI_
From column: _data / dates / BirthURI_
``` python
if getValue("birth"):
    return getValue('uri')+"/birth/date"
else:
    return ""
```

#### _NotInUse_
From column: _data / dates / BirthDateURI_
``` python

```

#### _DeathURI_
From column: _data / dates / BirthURI_
``` python
if getValue("death"):
    return getValue('uri')+"/death"
else:
    return ""
```

#### _DeathDateURI_
From column: _data / dates / BirthDateURI_
``` python
if getValue("death"):
    return getValue('uri')+"/death/date"
else:
    return ""
```

#### _NotInUse1_
From column: _data / dates / NotInUse_
``` python

```

#### _NotInUse2_
From column: _data / dates / NotInUse1_
``` python

```

#### _UlanURI_
From column: _data / ulan_id_
``` python
if getValue("ulan_id"):
    return "http://vocab.getty.edu/ulan/"+getValue("ulan_id")
else:
    return ""
```

#### _BirthLatest_
From column: _data / dates / birth_
``` python
if getValue("birth"):
    return getValue("birth")+"-12-31"
else:   
    return ""
```

#### _DeathLatest_
From column: _data / dates / death_
``` python
if getValue("death"):
    return getValue("death")+"-12-31"
else:
    return ""
```

#### _NationalityURI_
From column: _data / locations / nationality_
``` python
return UM.uri_from_fields("thesauri/nationality/",getValue("nationality"))
```

#### _BirthLocation_
From column: _data / locations / birth_
``` python
if getValue("birth"):
    return UM.uri_from_fields("thesauri/location/",getValue("birth"))
else:
    return ""
```

#### _DeathLocation_
From column: _data / locations / death_
``` python
if getValue("death"):
    return UM.uri_from_fields("thesauri/location/",getValue("death"))
else:
    return ""
```

#### _BirthEarliest_
From column: _data / dates / birth_
``` python
if getValue("birth"):
    return getValue("birth")+"-01-01"
else:
    return ""
```

#### _DeathEarliest_
From column: _data / dates / death_
``` python
if getValue("death"):
    return getValue("death")+"-01-01"
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BirthDateURI_ | `uri` | `crm:E52_Time-Span1`|
| _BirthEarliest_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _BirthLatest_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _BirthLocation_ | `uri` | `crm:E53_Place1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _DeathDateURI_ | `uri` | `crm:E52_Time-Span2`|
| _DeathEarliest_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span2`|
| _DeathLatest_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span2`|
| _DeathLocation_ | `uri` | `crm:E53_Place2`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _FamilyNameClassURI_ | `uri` | `crm:E82_Actor_Appellation5`|
| _FamilyNameTypeClassURI_ | `uri` | `crm:E55_Type3`|
| _GenderClassURI_ | `uri` | `crm:E55_Type5`|
| _GenderTypeClassURI_ | `uri` | `crm:E55_Type6`|
| _GivenNameClassURI_ | `uri` | `crm:E82_Actor_Appellation3`|
| _GivenNameTypeClass_ | `uri` | `crm:E55_Type1`|
| _MiddleNameClassURI_ | `uri` | `crm:E82_Actor_Appellation4`|
| _MiddleNameTypeClassURI_ | `uri` | `crm:E55_Type2`|
| _NameSuffixClassURI_ | `uri` | `crm:E82_Actor_Appellation6`|
| _NameSuffixTypeClassURI_ | `uri` | `crm:E55_Type4`|
| _NameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _NationalityURI_ | `uri` | `crm:E74_Group1`|
| _UlanURI_ | `uri` | `skos:Concept1`|
| _birth_ | `rdfs:label` | `crm:E53_Place1`|
| _birthdatelabel_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _death_ | `rdfs:label` | `crm:E53_Place2`|
| _deathdatelabel_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _fullnamelabel_ | `rdfs:label` | `crm:E39_Actor1`|
| _name_first_ | `rdf:value` | `crm:E82_Actor_Appellation3`|
| _name_full_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _name_last_ | `rdf:value` | `crm:E82_Actor_Appellation5`|
| _name_middle_ | `rdf:value` | `crm:E82_Actor_Appellation4`|
| _name_suffix_ | `rdf:value` | `crm:E82_Actor_Appellation6`|
| _nationality_ | `rdfs:label` | `crm:E74_Group1`|
| _sex_ | `rdfs:label` | `crm:E55_Type5`|
| _ulan_id_ | `rdfs:label` | `skos:Concept1`|
| _uri_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P2_has_type` | `crm:E55_Type5`|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation2`|
| `crm:E39_Actor1` | `skos:exactMatch` | `skos:Concept1`|
| `crm:E55_Type1` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404651`|
| `crm:E55_Type2` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404654`|
| `crm:E55_Type3` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404652`|
| `crm:E55_Type4` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300404662`|
| `crm:E55_Type5` | `crm:P2_has_type` | `crm:E55_Type6`|
| `crm:E55_Type6` | `skos:broadMatch` | `http://vocab.getty.edu/aat/300055147`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E64_End_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place2`|
| `crm:E74_Group1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300379842`|
| `crm:E82_Actor_Appellation2` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation3`|
| `crm:E82_Actor_Appellation2` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation4`|
| `crm:E82_Actor_Appellation2` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation5`|
| `crm:E82_Actor_Appellation2` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation6`|
| `crm:E82_Actor_Appellation3` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E82_Actor_Appellation4` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E82_Actor_Appellation5` | `crm:P2_has_type` | `crm:E55_Type3`|
| `crm:E82_Actor_Appellation6` | `crm:P2_has_type` | `crm:E55_Type4`|
| `skos:Concept1` | `skos:inScheme` | `http://vocab.getty.edu/ulan`|
