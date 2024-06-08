import requests
from requests.auth import HTTPBasicAuth

URL = 'https://py-api-srv:443'
headers = {'Content-Type': 'application/json' }
basic_auth = HTTPBasicAuth('user', 'pass')

def send_request(endpoint):
    return requests.get(URL + endpoint, headers=headers, auth=basic_auth, verify=False)

def send_request_list(endpoint, values: list):
    var_builder = "/".join(values)
    return requests.get(URL + endpoint + '/' + var_builder, headers=headers, auth=basic_auth, verify=False)
