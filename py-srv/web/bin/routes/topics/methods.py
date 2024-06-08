from routes.const import send_request, send_request_list
from flask import Blueprint, render_template

def route_web():

    PREFIX = '/topics'

    topics_web = Blueprint('topics_web', __name__, url_prefix=PREFIX, template_folder='templates')

    def render_view(res: dict, name='/', page=1):
        return render_template("topics.html", count=res['count'], page=page, \
                               maxPage=res['max_page'], response=res['response'], \
                                aggregation = res['aggregation'], search_term=name)

    @topics_web.route('/')
    def get_all():
        res: dict = send_request(PREFIX + '/')
        return render_view(res)

    @topics_web.route('/<topic>')
    def search_by_topic(topic):
        res: dict = send_request_list(PREFIX, [topic])
        return render_view(res, topic)

    @topics_web.route('/<int:page>/<topic>')
    def search_by_topic_by_page(page, topic):
        res: dict = send_request_list(PREFIX, [page, topic])
        return render_view(res, topic, page)
    
    return topics_web