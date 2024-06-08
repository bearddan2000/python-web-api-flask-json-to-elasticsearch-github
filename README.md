# python-web-api-flask-json-to-elasticsearch-github

## Description
Creates an api of `git-repo` for a flask project by loading json into elasticsearch. 

Elasticsearch DSL is used to build a proxy connection to the `elasticsearch` service.

Has the ability to query by parameters and pagination.

Uses redis as a cache layer for queries.

## Security
Self-signed ssl certificate for both web and api requests.
Requires basic authentication for endpoints.

| username | password |
| -------- | -------- |
| *user* | *pass* |

## Testing
Unit tests ran when program begins.
Remotely tested with *testify*, the ssl is not verified.

## Tech stack
- python
  - flask
  - flask-httpauth
  - pyopenssl
  - elasticsearch
  - redis
  - unittest
  - testify

## Docker stack
- python:latest
- elasticsearch
- kibana
- redis

## To run
`sudo ./install.sh -u`
- [Web page availble here](https://localhost)
- [Endpoints](endpoints.md)

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credits
- [Elasticsearch pagination](https://logfetch.com/elasticsearch-scroll-python/)
- [Elasticsearch terms aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-multi-terms-aggregation.html)
- [Flask blueprint tutorial](https://realpython.com/flask-blueprint/)
- [Flask blueprint pass args](https://stackoverflow.com/questions/28640081/how-to-pass-arbitrary-arguments-to-a-flask-blueprint)
- [Flask redis elasticsearch example](https://github.com/lakshaysinghal/indexingapi/blob/master/daemon.py)
- [Selenium in Docker](https://stackoverflow.com/questions/66597600/how-to-connect-to-standalone-selenium-firefox-container-from-another-container)
- [Selenium for python](https://selenium-python.readthedocs.io/)
- [All endpoints for flask app](https://github.com/pallets/flask/blob/2.1.2/src/flask/cli.py#L931)