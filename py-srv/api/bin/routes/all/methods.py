from flask import Blueprint

def route_api(client, auth):

    all_api = Blueprint('all_api', __name__, url_prefix='/api')

    @all_api.route('/')
    @auth.login_required
    def get_all():
        return client.get_all()

    @all_api.route('/<int:page>')
    @auth.login_required
    def get_all_by_page(page):
        return client.get_all(page)
    
    return all_api

