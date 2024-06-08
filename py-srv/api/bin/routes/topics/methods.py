from flask import Blueprint

def route_api(client, auth):

    topics_api = Blueprint('topics_api', __name__, url_prefix='/api/topics')

    @topics_api.route('/<topic>')
    @auth.login_required
    def search_by_topic(topic):
        return client.search_by_topic(topic)

    @topics_api.route('/<int:page>/<topic>')
    @auth.login_required
    def search_by_topic_by_page(page, topic):
        return client.search_by_topic(topic, page)
    
    return topics_api
