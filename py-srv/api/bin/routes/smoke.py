from flask import Blueprint

def route_api(auth):
    """used for remote testing"""
    smoke_test = Blueprint('smoke_test', __name__)

    @smoke_test.route('/smoke')
    @auth.login_required
    def hello_world():
        return {'msg': 'hello world'}
    
    return smoke_test
