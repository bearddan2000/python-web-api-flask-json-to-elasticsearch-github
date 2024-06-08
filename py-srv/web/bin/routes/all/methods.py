from flask import Blueprint, render_template
from routes.const import send_request, send_request_list

def route_web():

    PREFIX = ''

    all_web = Blueprint('all_web', __name__, \
                        url_prefix=PREFIX, \
                        template_folder='templates')

    def render_view(res: dict, name: str='', page=1):
        return render_template("index.html", search="Name", count=res['count'], \
                               page=page, maxPage=res['max_page'], response=res['response'], \
                                aggregation = res['aggregation'], search_term=name)

    @all_web.route('/')
    def get_all():
        res: dict=send_request(PREFIX+'/')
        return render_view(res)

    @all_web.route('/<int:page>')
    def get_all_by_page(page):
        res: dict=send_request_list(PREFIX, [page])
        return render_view(res, page=page)
    
    return all_web
