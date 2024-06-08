import logging, ast
from elasticsearch import Elasticsearch
from redis import Redis

from query.cls_aggregation import Aggregation

INDEX_NAME = "git-repo"

logging.basicConfig(level=logging.INFO)

class Query():

    def __init__(self, server: Elasticsearch) -> None:
        self.es = server

    def dict_hash(self, dictionary):
        import hashlib, json

        """MD5 hash of a dictionary."""
        dhash = hashlib.md5()
        # We need to sort arguments so {'a': 1, 'b': 2} is
        # the same as {'b': 2, 'a': 1}
        encoded = json.dumps(dictionary, sort_keys=True).encode()
        dhash.update(encoded)
        return dhash.hexdigest()

    def paginated_scroll(self, query, scroll, size, **kw):
        """generator for scroll api"""
        page = self.es.search(index=INDEX_NAME, query=query, scroll=scroll, size=size, **kw)
        scroll_id = page['_scroll_id']
        hits = page['hits']['hits']

        while len(hits):
            yield hits
            page = self.es.scroll(scroll_id=scroll_id, scroll=scroll)
            scroll_id = page['_scroll_id']
            hits = page['hits']['hits']

    def redis_exists(self, redis_value: str, DELIMITER: str) -> list:
        result: list = []    

        # split to a list
        for d in redis_value.split(DELIMITER):
            # convert from str to dict
            tmp = ast.literal_eval(d)
            result.append(tmp)
        return result

    def redis_loop(self, i: int, value: str, redis_value: str, DELIMITER: str) -> str:
        if i == 0:
            redis_value = str(value)
        else:
            redis_value += DELIMITER + str(value)
        return redis_value

    def refresh_results(self, QUERY, page: int):
        
        RESULT_LIMIT = 1
        DELIMITER = '::'
        redis_key = str(QUERY)
        i = 0
        result: list = []
        redis = Redis(host="redis")
        aggregation = Aggregation()
        buckets = {
            'build': {},
            'catagory': {}, 
            'language':{},
            'platform': {},
            'subcatagory': {},
            'tech': {}, 
            'topics': {}
        }
        key = self.dict_hash(QUERY)

        if redis.exists(redis_key):
            # convert from bytes to str
            redis_value = str(redis.get(redis_key), 'UTF-8')
            result = self.redis_exists(redis_value=redis_value, DELIMITER=DELIMITER)
            i = len(result)
            buckets = aggregation.aggregation_cache[key]
        else:
            i = 0
            result: list = []
            redis_value = ''
            gen = self.paginated_scroll(QUERY, '2s', RESULT_LIMIT)
            for hits in gen:
                for hit in hits:
                    value = hit['_source']
                    redis_value = self.redis_loop(i, value, redis_value, DELIMITER)
                    result.append(value)
                    i += 1
                    aggregation.aggregate_language_count(value, buckets['language'])
                    aggregation.aggregate_generic_filter_count(value, 'build', buckets['build'])
                    aggregation.aggregate_generic_filter_count(value, 'platform', buckets['platform'])
                    aggregation.aggregate_generic_filter_count(value, 'tech', buckets['tech'])
                    aggregation.aggregate_topic_count(value, buckets['topics'])
                    aggregation.aggregate_generic_catagory_count(value, 'catagory', buckets['catagory'])
                    aggregation.aggregate_generic_catagory_count(value, 'subcatagory', buckets['subcatagory'])
            redis.set(redis_key, redis_value)

            aggregation.aggregation_cache[key] = buckets

        return aggregation.aggregate_results(QUERY, i, page, result, RESULT_LIMIT)
