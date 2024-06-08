import logging

logging.basicConfig(level=logging.INFO)

class Filter():
    def __init__(self, topics: list, build_const, platform_const, language_const, tech_const):
        keywords: list = topics.copy()
        self.build = self.filter_assign(keywords, build_const)
        self.platform = self.filter_assign(keywords, platform_const)
        self.language = self.filter_assign(keywords, language_const)
        self.tech = self.filter_assign(keywords, tech_const)

    def filter_assign(self, keywords, known_list):
        """ find and assign filter value from known_list"""
        result = self.filter_value(keywords, known_list)
        if result is None:
            return {'name': 'unclass', 'color': 'pink'}
        return result

    def filter_value(self, keywords, known_list):
        """
        1. iterate keywords
        2. iterate known list
        3. return match
        """
        for x in keywords:
            for y in known_list:
                if x == y['name']:
                    keywords.remove(x)
                    return y
        return None
    
class Process():
    
    def __init__(self, name, catagory_const, build_const, platform_const, language_const, tech_const) -> None:
        self.name = name
        self.topics = []
        self.compose_desc()
        self.compose_topics()
        self.filter = Filter(self.topics,build_const, platform_const, language_const, tech_const)
        self.catagory = self.compose_catagory(self.topics, catagory_const)

    def distinct_list(self, tmp_lst):
        """
        1. remove duplicates
        2. add to topics
        """
        condensed_lst = list(set(tmp_lst))
        for item in condensed_lst:
            self.topics.append(item)

    def compose_desc(self):
        self.desc = '-'

    def compose_topics(self):
        """create unique list of topics"""
        tmp_lst = []
        for item in self.name.split("-"):
            tmp_lst.append(item)
        self.distinct_list(tmp_lst)

    def compose_catagory(self, keywords: list, known_list: list):
        """
        1. iterate keywords
        2. check know_dict for entry
        3. add dict value to list
        4. remove duplicates
        5. return list
        """
        catagory_list =  []
        topic_list =  []
        for x in keywords:
            for y in known_list:
                try:
                    value = y[x]
                    catagory_list.append(value)
                    topic_list.append(value['catagory'])
                    topic_list.append(value['subcatagory'])
                except:
                    continue
        self.distinct_list(topic_list)
        return catagory_list
