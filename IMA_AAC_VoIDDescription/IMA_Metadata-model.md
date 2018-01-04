# Data_IMA_metadata.json

## Add Column

## Add Node/Literal

## PyTransforms
#### _HomepageURL_
From column: _Homepage_
``` python
return getValue("Homepage")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Classes_ | `http://rdfs.org/ns/void#classes` | `Dataset1`|
| _Contributor_ | `dct:contributor` | `Dataset1`|
| _Created_ | `dct:created` | `Dataset1`|
| _Creator_ | `dct:creator` | `Dataset1`|
| _DatasetDescription_ | `uri` | `DatasetDescription1`|
| _DatasetDescriptionCreator_ | `dct:creator` | `DatasetDescription1`|
| _DatasetDescriptionTitle_ | `dct:title` | `DatasetDescription1`|
| _Dataset_URI_ | `uri` | `Dataset1`|
| _Date_ | `dct:date` | `Dataset1`|
| _Description_ | `dct:description` | `Dataset1`|
| _Entities_ | `http://rdfs.org/ns/void#entities` | `Dataset1`|
| _Example_resource_ | `http://rdfs.org/ns/void#exampleResource` | `Dataset1`|
| _Homepage_ | `uri` | `foaf:Document1`|
| _Issued_ | `dct:issued` | `Dataset1`|
| _License_ | `dct:license` | `Dataset1`|
| _Modified_ | `dct:modified` | `Dataset1`|
| _Properties_ | `http://rdfs.org/ns/void#properties` | `Dataset1`|
| _Publisher_ | `dct:publisher` | `Dataset1`|
| _RDF_data_dump_ | `http://rdfs.org/ns/void#dataDump` | `Dataset1`|
| _Sparql_endpoint_ | `http://rdfs.org/ns/void#sparqlEndpoint` | `Dataset1`|
| _Subject_ | `dct:subject` | `Dataset1`|
| _Technical_feature_ | `http://rdfs.org/ns/void#feature` | `Dataset1`|
| _Title_ | `dct:title` | `Dataset1`|
| _Triples_ | `http://rdfs.org/ns/void#triples` | `Dataset1`|
| _URI_pattern_ | `http://rdfs.org/ns/void#uriSpace` | `Dataset1`|
| _values_ | `http://rdfs.org/ns/void#vocabulary` | `Dataset1`|
| _values_ | `dct:source` | `Dataset1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `Dataset1` | `foaf:homepage` | `foaf:Document1`|
| `DatasetDescription1` | `foaf:primaryTopic` | `Dataset1`|
