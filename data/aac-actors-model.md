# aac-actors.json

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

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
return "id/"+getValue('firstid')
```

#### _NameURI_
From column: _data / uri_
``` python
return "nameobject/"+getValue('uri')
```

#### _GivenNameClassURI_
From column: _data / NameURI_
``` python
return "nameobject/givenname/"+getValue('uri')
```

#### _GivenNameTypeClass_
From column: _data / GivenNameClassURI_
``` python
return "nameobject/givenname/givennametype/"+getValue('uri')
```

#### _MiddleNameClassURI_
From column: _data / GivenNameClassURI_
``` python
return "nameobject/middlename/"+getValue('uri')
```

#### _MiddleNameTypeClassURI_
From column: _data / MiddleNameClassURI_
``` python
return "nameobject/middlename/middlenametype/"+getValue('uri')
```

#### _FamilyNameClassURI_
From column: _data / GivenNameClassURI_
``` python
return "nameobject/familyname/"+getValue('uri')
```

#### _FamilyNameTypeClassURI_
From column: _data / FamilyNameClassURI_
``` python
return "nameobject/familyname/familynametype/"+getValue('uri')
```

#### _NameSuffixClassURI_
From column: _data / MiddleNameClassURI_
``` python
return "nameobject/namesuffix/"+getValue('uri')
```

#### _NameSuffixTypeClassURI_
From column: _data / NameSuffixClassURI_
``` python
return "nameobject/namesuffix/namesuffixtype/"+getValue('uri')
```

#### _ActorClassURI_
From column: _data / NameURI_
``` python
return "nameobject/actor/"+getValue('uri')
```

#### _GenderClassURI_
From column: _data / NameSuffixClassURI_
``` python
return "gender/"+getValue('uri')
```

#### _GenderTypeClassURI_
From column: _data / GenderClassURI_
``` python
return "gender/gendertype/"+getValue('uri')
```

#### _birthdatelabel_
From column: _data / dates / birth_
``` python
return getValue("birth")
```

#### _deathdatelabel_
From column: _data / dates / death_
``` python
return getValue("death")
```

#### _BirthURI_
From column: _data / dates / birth_
``` python
return "birthobject/"+getValue('uri')
```

#### _BirthDateURI_
From column: _data / dates / BirthURI_
``` python
return "birthobject/birthdate/"+getValue('uri')
```

#### _BirthPlaceURI_
From column: _data / dates / BirthDateURI_
``` python
return "birthobject/birthplace/"+getValue('uri')
```

#### _DeathURI_
From column: _data / dates / BirthURI_
``` python
return "deathobject/"+getValue('uri')
```

#### _DeathDateURI_
From column: _data / dates / BirthDateURI_
``` python
return "deathobject/deathdate/"+getValue('uri')
```

#### _DeathPlaceURI_
From column: _data / dates / BirthPlaceURI_
``` python
return "deathobject/deathplace/"+getValue('uri')
```

#### _NationalityClassURI_
From column: _data / dates / DeathPlaceURI_
``` python
return "nationalityobject/"+getValue('uri')
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ActorClassURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _BirthDateURI_ | `uri` | `crm:E52_Time-Span1`|
| _BirthPlaceURI_ | `uri` | `crm:E53_Place1`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _DeathDateURI_ | `uri` | `crm:E52_Time-Span2`|
| _DeathPlaceURI_ | `uri` | `crm:E53_Place2`|
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
| _NationalityClassURI_ | `uri` | `crm:E74_Group1`|
| _birth_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _birth_ | `rdfs:label` | `crm:E53_Place1`|
| _birthdatelabel_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _death_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span2`|
| _death_ | `rdfs:label` | `crm:E53_Place2`|
| _deathdatelabel_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _fullnamelabel_ | `rdfs:label` | `crm:E39_Actor1`|
| _name_first_ | `rdf:value` | `crm:E82_Actor_Appellation3`|
| _name_full_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _name_last_ | `rdf:value` | `crm:E82_Actor_Appellation5`|
| _name_middle_ | `rdf:value` | `crm:E82_Actor_Appellation4`|
| _name_suffix_ | `rdf:value` | `crm:E82_Actor_Appellation6`|
| _nationality_ | `rdfs:label` | `crm:E74_Group1`|
| _sex_ | `rdfs:label` | `crm:E55_Type5`|
| _uri_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P2_has_type` | `crm:E55_Type5`|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation2`|
| `crm:E55_Type1` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404651`|
| `crm:E55_Type2` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404654`|
| `crm:E55_Type3` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404652`|
| `crm:E55_Type4` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404662`|
| `crm:E55_Type5` | `crm:P2_has_type` | `crm:E55_Type6`|
| `crm:E55_Type6` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300055147`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E64_End_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place2`|
| `crm:E74_Group1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300379842`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
| `crm:E82_Actor_Appellation2` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation3`|
| `crm:E82_Actor_Appellation2` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation4`|
| `crm:E82_Actor_Appellation2` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation5`|
| `crm:E82_Actor_Appellation2` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation6`|
| `crm:E82_Actor_Appellation3` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E82_Actor_Appellation4` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E82_Actor_Appellation5` | `crm:P2_has_type` | `crm:E55_Type3`|
| `crm:E82_Actor_Appellation6` | `crm:P2_has_type` | `crm:E55_Type4`|
