import logging
from elasticsearch import Elasticsearch
from query.const import *
from query.cls_query import Query

logging.basicConfig(level=logging.INFO)

class Endpoints():
    def __init__(self, server: Elasticsearch) -> None:
        self.es = server
        self.q = Query(server)

    def search_by_build(self, build, page):
        TERM = term_builder("filter.build.name", build)
        return self.q.refresh_results(TERM, page)
    
    def search_by_language(self, language, page):
        TERM = term_builder("filter.language.name", language)
        return self.q.refresh_results(TERM, page)
    
    def search_by_language_build(self, build, language, page):
        MULTI = multi_should_builder("filter.build.name", build, language)
        return self.q.refresh_results(MULTI, page)
    
    def search_by_language_platform(self, platform, language, page):
        MULTI = multi_should_builder("filter.platform.name", platform, language)
        return self.q.refresh_results(MULTI, page)
    
    def search_by_platform(self, platform, page):
        TERM = term_builder("filter.platform.name", platform)
        return self.q.refresh_results(TERM, page)
    
    def search_by_tech(self, tech, page):
        TERM = term_builder("filter.tech.name", tech)
        return self.q.refresh_results(TERM, page)
    
    def search_by_topic(self, topic, page):
        TERM = term_builder("topics", topic)
        return self.q.refresh_results(TERM, page)
    
    def search_by_catagory(self, catagory, page):
        TERM = term_builder("catagory.catagory", catagory)
        return self.q.refresh_results(TERM, page)
    
    def search_by_subcatagory(self, catagory, page):
        TERM = term_builder("catagory.subcatagory", catagory)
        return self.q.refresh_results(TERM, page)
    
    def search_by_name(self, name, page):
        WILDCARD = wildcard_builder("name", name)
        return self.q.refresh_results( WILDCARD, page)

    def get_all(self, page):
        return self.q.refresh_results(SELECT_ALL, page)

