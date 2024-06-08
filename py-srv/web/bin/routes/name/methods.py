from flask import Blueprint, render_template
from routes.const import send_request_list

def route_web():

    PREFIX = '/name'

    name_web = Blueprint('name_web', __name__, \
                        url_prefix=PREFIX, \
                        template_folder='templates')

    def render_view(res: dict, name: str, page=1):
        """
            index.html is found in route/name/templates
        """
        return render_template("name.html", search="Name", count=res['count'], \
                               page=page, maxPage=res['max_page'], response=res['response'], \
                                aggregation = res['aggregation'], search_term=name)
    
    @name_web.route('/<name>')
    def get_name(name):
        res: dict=send_request_list(PREFIX, [name])
        return render_view(res, name)
    
    @name_web.route('/<int:page>/<name>')
    def get_name_by_page(page, name):
        res: dict=send_request_list(PREFIX, [page, name])
        return render_view(res, name, page)
    
    return name_web
