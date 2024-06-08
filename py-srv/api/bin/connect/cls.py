import logging
from typing import Any, Dict, Optional
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from flask import Flask, _app_ctx_stack

logging.basicConfig(level=logging.INFO)

class ElasticsearchConnect():
    server_name = ''

    def __init__(self, app:Flask, server) -> None:
        self.server_name = server
        conn = ElasticsearchProxy(app, server)
        self.es = conn.connect()
        logging.info(self.es.ping())
        
class ElasticsearchProxy:
    """Proxy for Elasticsearch connection that works with Flask.

    Documentation for Elasticseach:
      https://elasticsearch-py.readthedocs.io

    Documentation for Elasticseach DSL:
      https://elasticsearch-dsl.readthedocs.io
    """

    def __init__(self, app: Flask, server):
        self.app = app
        self.server = server
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        app.config.setdefault('ELASTICSEARCH_HOST', self.server)
        app.config.setdefault('ELASTICSEARCH_TIMEOUT', 30)
        app.config.setdefault('ELASTICSEARCH_USERNAME', 'elasticsearch')
        app.config.setdefault('ELASTICSEARCH_PASSWORD', 'changeme')

        app.teardown_appcontext(self.teardown)

    def connect(self) -> Elasticsearch:

        host = self.server
        if not host:
            raise RuntimeError(
                'Cannot connect to elastic search without a host')

        options: Dict[str, Any] = {
            'hosts': [host],
        }

        username = 'elasticsearch'
        password = 'changeme'

        if username and password:
            options['http_auth'] = (username, password)

        timeout = 10
        if timeout is not None:
            options['timeout'] = timeout

        return connections.create_connection(**options)

    def teardown(self, exception: Optional[Exception]) -> None:
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'elasticsearch'):
            connections.remove_connection('default')
            ctx.elasticsearch = None
