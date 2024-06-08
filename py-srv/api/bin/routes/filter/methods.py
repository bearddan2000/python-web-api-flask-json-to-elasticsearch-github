import logging
from flask import Blueprint

logging.basicConfig(level=logging.INFO)

def route_api(client, auth):

    filters_api = Blueprint('filters_api', __name__, url_prefix='/api/filter')

    @filters_api.route('/build/<filter>')
    @auth.login_required
    def search_by_build(filter):
        return client.search_by_build(filter)

    @filters_api.route('/<int:page>/build/<filter>')
    @auth.login_required
    def search_by_build_by_page(page, filter):
        return client.search_by_build(filter, page)
    
    @filters_api.route('/language/<filter>')
    @auth.login_required
    def search_by_language(filter):
        return client.search_by_language(filter)

    @filters_api.route('/<int:page>/language/<filter>')
    @auth.login_required
    def search_by_language_by_page(page, filter):
        return client.search_by_language(filter, page)
    
    @filters_api.route('/language/<language>/build/<build>')
    @auth.login_required
    def search_by_language_build(language, build):
        return client.search_by_language_build(language, build)

    @filters_api.route('/<int:page>/language/<language>/build/<build>')
    @auth.login_required
    def search_by_language_build_by_page(page, language, build):
        return client.search_by_language_build(language, build, page)
    
    @filters_api.route('/language/<language>/platform/<platform>')
    @auth.login_required
    def search_by_language_platform(language, platform):
        res: dict = client.search_by_language_platform(language, platform)

    @filters_api.route('/<int:page>/language/<language>/platform/<platform>')
    @auth.login_required
    def search_by_language_platform_by_page(page, language, platform):
        return client.search_by_language_platform(language, platform, page)
    
    @filters_api.route('/platform/<filter>')
    @auth.login_required
    def search_by_platform(filter):
        return client.search_by_platform(filter)

    @filters_api.route('/<int:page>/platform/<filter>')
    @auth.login_required
    def search_by_platform_by_page(page, filter):
        return client.search_by_platform(filter, page)
    
    @filters_api.route('/tech/<filter>')
    @auth.login_required
    def search_by_tech(filter):
        return client.search_by_tech(filter)

    @filters_api.route('/<int:page>/tech/<filter>')
    @auth.login_required
    def search_by_tech_by_page(page, filter):
        return client.search_by_tech(filter, page)
    
    return filters_api


