from flask import Blueprint

def route_api(client, auth):

    name_api = Blueprint('name_api', __name__, url_prefix='/api/name')

    @name_api.route('/<name>')
    @auth.login_required
    def get_name(name):
        return client.search_by_name(name)

    @name_api.route('/<int:page>/<name>')
    @auth.login_required
    def get_name_by_page(page, name):
        return client.search_by_name(name, page)
    
    return name_api
