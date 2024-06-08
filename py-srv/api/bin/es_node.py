from flask import Flask

from connect.cls import ElasticsearchConnect
from query.cls_endpoint import Endpoints
from query.cls_seed import Seed

class Cluster():

    def __init__(self, app:Flask, server) -> None:
        es = self.connect(app, server)
        Seed(es)
        self.endpoint = Endpoints(es)

    def connect(self, app:Flask, server):
        o = ElasticsearchConnect(app, server)
        return o.es

    def search_by_build(self, build, page=1):
        return self.endpoint.search_by_build(build, page)
    
    def search_by_language(self, language, page=1):
        return self.endpoint.search_by_language(language, page)
    
    def search_by_language_build(self, language, build, page=1):
        return self.endpoint.search_by_language_build(build, language, page)
    
    def search_by_language_platform(self, language, platform, page=1):
        return self.endpoint.search_by_language_platform(platform, language, page)
    
    def search_by_platform(self, platform, page=1):
        return self.endpoint.search_by_platform(platform, page)
    
    def search_by_tech(self, tech, page=1):
        return self.endpoint.search_by_tech(tech, page)
    
    def search_by_topic(self, topic, page=1):
        return self.endpoint.search_by_topic(topic, page)
    
    def search_by_catagory(self, catagory, page=1):
        return self.endpoint.search_by_catagory(catagory, page)
    
    def search_by_subcatagory(self, catagory, page=1):
        return self.endpoint.search_by_subcatagory(catagory, page)

    def get_all(self, page=1):
        return self.endpoint.get_all(page)
    
    def search_by_name(self, name, page=1):
        return self.endpoint.search_by_name(name, page)