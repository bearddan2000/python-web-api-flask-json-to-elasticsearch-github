
configurations = {
    "settings": {
        "index": {"number_of_replicas": 2},
        "analysis": {
            "filter": {
                "ngram_filter": {
                    "type": "edge_ngram",
                    "min_gram": 2,
                    "max_gram": 15,
                },
            },
            "analyzer": {
                "ngram_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "ngram_filter"],
                },
            },
        },
    },
    "mappings": {
        "properties": {
            'name': {
                "type": 'keyword'
            }, 
            'desc': {
                "type": 'text',
                "analyzer": "standard"
            },
            'topics': {
                "type": 'keyword'
            },
            "filter.build.name": {
                "type": "keyword"
            },
            "filter.build.color": {
                "type": "text"
            },
            "filter.language.name": {
                "type": "keyword"
            },
            "filter.language.color": {
                "type": "text"
            },
            "filter.platform.name": {
                "type": "keyword"
            },
            "filter.platform.color": {
                "type": "text"
            },
            "filter.tech.name": {
                "type": "keyword"
            },
            "filter.tech.color": {
                "type": "text"
            },
            "catagory.catagory": {
                "type": "keyword"
            },
            "catagory.subcatagory": {
                "type": "keyword"
            }
        }
    },
}
