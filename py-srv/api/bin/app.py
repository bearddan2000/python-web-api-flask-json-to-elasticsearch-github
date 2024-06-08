from flask import Flask
from flask_httpauth import HTTPBasicAuth
import routes.topics.methods, routes.smoke
import routes.name.methods
import routes.filter.methods
import routes.catagory.methods
import routes.all.methods
from es_node import Cluster

auth = HTTPBasicAuth()

app = Flask(__name__)

client = Cluster(app, 'elasticsearch')

users = {'user': 'pass'}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        if password in users[username]: 
            return True
    return False

app.register_blueprint(routes.all.methods.route_api(client, auth))

app.register_blueprint(routes.catagory.methods.route_api(client, auth))

app.register_blueprint(routes.filter.methods.route_api(client, auth))

app.register_blueprint(routes.name.methods.route_api(client, auth))

app.register_blueprint(routes.smoke.route_api(auth), url_prefix='/api')

app.register_blueprint(routes.topics.methods.route_api(client, auth))
 
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 443, debug = True,  ssl_context='adhoc')
