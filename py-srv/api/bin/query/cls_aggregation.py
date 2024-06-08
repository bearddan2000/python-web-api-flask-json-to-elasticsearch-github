import logging, math

logging.basicConfig(level=logging.INFO)

class Aggregation():
    """pandas wont work here bc we deal with a jagged collection"""
    def __init__(self) -> None:
        self.aggregation_cache = {}
        
    def aggregate_topic_count(self, value: str, buckets):
        bucket_key = value['topics']
        for item in bucket_key:
            if item not in buckets:
                buckets[item] = {
                    'value': 1
                } 
            else:
                buckets[item] = {
                    'value': buckets[item]['value']+1
                }

    def aggregate_generic_filter_count(self, value: str, sub_group, buckets):
        bucket_key = value['filter'][sub_group]['name']
        color = value['filter'][sub_group]['color']
        if bucket_key not in buckets:
            buckets[bucket_key] = {
                'value': 1, 'color': color
            } 
        else:
            buckets[bucket_key] = {
                'value': buckets[bucket_key]['value']+1, \
                'color': color
            }

    def aggregate_generic_catagory_count(self, value: str, sub_group, buckets):
        bucket_key = value['catagory']
        for item in bucket_key:
            x = item[sub_group]
            if x not in buckets:
                buckets[x] = {
                    'value': 1
                } 
            else:
                buckets[x] = {
                    'value': buckets[x]['value']+1
                }

    def aggregate_language_count(self, value: str, buckets):
        bucket_key = value['filter']['language']['name']
        color = value['filter']['language']['color']
        if bucket_key not in buckets:
            buckets[bucket_key] = {
                'value': 1, 'color': color, \
                'build': self.aggregate_sub_count(value, 'build', {}), \
                'platform':  self.aggregate_sub_count(value, 'platform', {})
            }
        else:
            sub_build = buckets[bucket_key]['build']
            sub_platform = buckets[bucket_key]['platform']
            buckets[bucket_key] = {
                'value': buckets[bucket_key]['value']+1, \
                'color': color, \
                'build': self.aggregate_sub_count(value, 'build', sub_build), \
                'platform': self.aggregate_sub_count(value, 'platform', sub_platform)
            }
    
    def aggregate_sub_count(self, value, key_str, container):
        key = value['filter'][key_str]['name']
        color = value['filter'][key_str]['color']
        if key not in container:
            container[key] = {'value': 1, 'color': color} 
        else:
            container[key] = {
                'value': container[key]['value']+1, \
                'color': color
            }
        return container
    
    def aggregate_results(self, QUERY: dict, i: int, page: int, \
                          result: list, RESULT_LIMIT: int):

        ct = i
        key = self.dict_hash(QUERY)
        max_page = int(math.ceil(ct / RESULT_LIMIT)) or 1
        start: int = page * RESULT_LIMIT
        end = start + RESULT_LIMIT
        return { "response": result[start:end], "count": ct, \
                "max_page": max_page-1, "aggregation": self.aggregation_cache[key]}
