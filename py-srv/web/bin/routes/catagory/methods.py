from flask import Blueprint, render_template
from routes.const import send_request, send_request_list

def route_web():

    PREFIX = '/catagory'

    catagories_web = Blueprint('catagories_web', __name__, \
                               url_prefix=PREFIX, \
                                template_folder='templates')

    def render_view(res: dict, name: str = '/', page=1):
        return render_template("catagory.html", count=res['count'], \
                               page=page, maxPage=res['max_page'], response=res['response'], \
                                aggregation = res['aggregation'], search_term=name)
    
    @catagories_web.route('/')
    def get_all_catagory():
        res: dict = send_request(PREFIX + '/')
        return render_view(res)
    
    @catagories_web.route('/<catagory>')
    def search_by_catagory(catagory):
        res: dict = send_request_list(PREFIX, [catagory])
        return render_view(res, catagory)

    @catagories_web.route('/<int:page>/<catagory>')
    def search_by_catagory_by_page(page, catagory):
        res: dict = send_request_list(PREFIX, [page, catagory])
        return render_view(res, catagory, page)
    
    @catagories_web.route('/<catagory>/sub/<subcatagory>')
    def search_by_catagory_then_sub(catagory, subcatagory):
        res: dict = send_request_list(PREFIX, [catagory, 'sub', subcatagory])
        return render_view(res, catagory)

    @catagories_web.route('/<int:page>/<catagory>/sub/<subcatagory>')
    def search_by_catagory_then_sub_by_page(page, catagory, subcatagory):
        res: dict = send_request_list(PREFIX, [page, catagory, 'sub', subcatagory])
        return render_view(res, catagory, page)
        
    @catagories_web.route('/sub/<subcatagory>')
    def search_by_subcatagory(subcatagory):
        res: dict = send_request_list(PREFIX, ['sub', subcatagory])
        return render_view(res, subcatagory)
    
    @catagories_web.route('/<int:page>/sub/<subcatagory>')
    def search_by_subcatagory_by_page(page, subcatagory):
        res: dict = send_request_list(PREFIX, [page, 'sub', subcatagory])
        return render_view(res, subcatagory, page)
    
    return catagories_web