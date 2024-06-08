def term_builder(field, value):
    return {"bool": {"filter": {"term": {field: value}}}}

def prefix_builder(field, value):
    return {"bool": {"should": {"prefix": {field: value}}}}

def multi_should_builder(language_value, field, value):
    FIELD = "filter.language.name"
    return { 
        "bool": { 
            "filter": { 
                "term": { FIELD: language_value } 
            }
             ,
             "must": {
                 "match": { field: value }
             }
        }
    }

def wildcard_builder(field, value):
    val = "*"+value+"*"
    return {"wildcard": {field: {"value": val}}}


SELECT_ALL = {"match_all": {}}