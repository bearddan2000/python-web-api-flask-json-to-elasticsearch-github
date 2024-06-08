import logging
from flask import Blueprint, render_template

from routes.const import send_request, send_request_list

logging.basicConfig(level=logging.INFO)

def route_web():

    PREFIX = '/filter'

    filters_web = Blueprint('filters_web', __name__, url_prefix=PREFIX, template_folder='templates')

    def render_view(res: dict, name='/', page=1):
        logging.info(res)
        return render_template("filter.html", search="Filter", count=res['count'], \
                               page=page, maxPage=res['max_page'], response=res['response'], \
                               aggregation = res['aggregation'], search_term=name)

    @filters_web.route('/')
    def get_all():
        res: dict = send_request(PREFIX)
        return render_view(res)
    
    @filters_web.route('/build/<filter>')
    def search_by_build(filter):
        res: dict = send_request_list(PREFIX, ['build', filter])
        return render_view(res, filter)

    @filters_web.route('/<int:page>/build/<filter>')
    def search_by_build_by_page(page, filter):
        res: dict = send_request_list(PREFIX, [page, 'build', filter])
        return render_view(res, filter, page)
    
    @filters_web.route('/language/<filter>')
    def search_by_language(filter):
        res: dict = send_request_list(PREFIX, ['language', filter])
        return render_view(res, filter)

    @filters_web.route('/<int:page>/language/<filter>')
    def search_by_language_by_page(page, filter):
        res: dict = send_request_list(PREFIX, [page, 'language', filter])
        return render_view(res, filter, page)
    
    @filters_web.route('/language/<language>/build/<build>')
    def search_by_language_build(language, build):
        filter = f"{language}/build/{build}"
        res: dict = send_request_list(PREFIX, ['language', filter])
        return render_view(res, filter)

    @filters_web.route('/<int:page>/language/<language>/build/<build>')
    def search_by_language_build_by_page(page, language, build):
        filter = f"{language}/build/{build}"
        res: dict = send_request_list(PREFIX, [page, 'language', filter])
        return render_view(res, filter, page)
    
    @filters_web.route('/language/<language>/platform/<platform>')
    def search_by_language_platform(language, platform):
        filter = f"{language}/platform/{platform}"
        res: dict = send_request_list(PREFIX, ['language', filter])
        return render_view(res, filter)

    @filters_web.route('/<int:page>/language/<language>/platform/<platform>')
    def search_by_language_platform_by_page(page, language, platform):
        filter = f"{language}/platform/{platform}"
        res: dict = send_request_list(PREFIX, [page, 'language', filter])
        return render_view(res, filter, page)
    
    @filters_web.route('/platform/<filter>')
    def search_by_platform(filter):
        res: dict = send_request_list(PREFIX, ['platform', filter])
        return render_view(res, filter)

    @filters_web.route('/<int:page>/platform/<filter>')
    def search_by_platform_by_page(page, filter):
        res: dict = send_request_list(PREFIX, [page, 'platform', filter])
        return render_view(res, filter, page)
    
    @filters_web.route('/tech/<filter>')
    def search_by_tech(filter):
        res: dict = send_request_list(PREFIX, ['tech', filter])
        return render_view(res, filter)

    @filters_web.route('/<int:page>/tech/<filter>')
    def search_by_tech_by_page(page, filter):
        res: dict = send_request_list(PREFIX, [page, 'tech', filter])
        return render_view(res, filter, page)
    
    return filters_web