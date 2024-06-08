from flask import Blueprint

def route_api(client, auth):

    catagories_api = Blueprint('catagories_api', __name__, url_prefix='/api/catagory')

    @catagories_api.route('/<catagory>')
    @auth.login_required
    def search_by_catagory(catagory):
        return client.search_by_catagory(catagory)

    @catagories_api.route('/<int:page>/<catagory>')
    @auth.login_required
    def search_by_catagory_by_page(page, catagory):
        return client.search_by_catagory(catagory, page)
    
    @catagories_api.route('/sub/<subcatagory>')
    @auth.login_required
    def search_by_subcatagory(subcatagory):
        return client.search_by_subcatagory(subcatagory)

    @catagories_api.route('/<int:page>/sub/<subcatagory>')
    @auth.login_required
    def search_by_subcatagory_by_page(page, subcatagory):
        return client.search_by_subcatagory(subcatagory, page)
    
    return catagories_api

