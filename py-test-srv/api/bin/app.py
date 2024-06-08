import requests
from requests.auth import HTTPBasicAuth
import testify

from const import *

def fun_call(url: str, fun, auth: HTTPBasicAuth = None):
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    if auth is not None:
        return fun(url, headers=headers, auth=auth, verify=False)
    else:
        return fun(url, headers=headers, verify=False)
    
def assert_url(url: str, fun_ptr, code: int = 200, auth: HTTPBasicAuth = None):
    """assert that endpoint is valid"""
    
    resp = fun_call(url, fun_ptr, auth)

    testify.assert_equal(resp.status_code, code)

    return 0

class TestSmoke(testify.TestCase):
    """docstring for TestSmoke."""

    def test_unauth_smoke_url(self):
        return assert_url(SMOKE_TEST_URL_API, requests.get, code=401)
    
    def test_auth_smoke_url(self):
        return assert_url(SMOKE_TEST_URL_API, requests.get, auth=HTTPBasicAuth('user', 'pass'))

class TestGet(testify.TestCase):
    """docstring for TestGet."""

    def test_unauth_get_all_url_api(self):
        return assert_url(GET_ALL_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_auth_get_all_url_api(self):
        return assert_url(GET_ALL_URL_API, requests.get, auth=AUTH)
    
    def test_unauth_get_all_by_page_url_api(self):
        return assert_url(GET_ALL_BY_PAGE_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_auth_get_all_by_page_url_api(self):
        return assert_url(GET_ALL_BY_PAGE_URL_API, requests.get, auth=AUTH)
    
class TestName(testify.TestCase):
    """docstring for TestName."""

    def test_unauth_search_name_url_api(self):
        return assert_url(SEARCH_BY_NAME_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_unauth_search_name_by_page_url_api(self):
        return assert_url(SEARCH_BY_NAME_BY_PAGE_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_auth_search_name_url_api(self):
        return assert_url(SEARCH_BY_NAME_URL_API, requests.get, auth=AUTH)
    
    def test_auth_search_name_by_page_url_api(self):
        return assert_url(SEARCH_BY_NAME_BY_PAGE_URL_API, requests.get, auth=AUTH)
    
class TestTopic(testify.TestCase):
    """docstring for TestTopic."""

    def test_unauth_search_topic_url_api(self):
        return assert_url(SEARCH_BY_TOPIC_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_unauth_search_topic_by_page_url_api(self):
        return assert_url(SEARCH_BY_TOPIC_BY_PAGE_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_auth_search_topic_url_api(self):
        return assert_url(SEARCH_BY_TOPIC_URL_API, requests.get, auth=AUTH)
    
    def test_auth_search_topic_by_page_url_api(self):
        return assert_url(SEARCH_BY_TOPIC_BY_PAGE_URL_API, requests.get, auth=AUTH)

class TestCatagory(testify.TestCase):
    """docstring for TestCatagory."""

    def test_unauth_search_catagory_url_api(self):
        return assert_url(SEARCH_BY_CATAGORY_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_unauth_search_catagory_by_page_url_api(self):
        return assert_url(SEARCH_BY_CATAGORY_BY_PAGE_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_auth_search_catagory_url_api(self):
        return assert_url(SEARCH_BY_CATAGORY_URL_API, requests.get, auth=AUTH)
    
    def test_auth_search_catagory_by_page_url_api(self):
        return assert_url(SEARCH_BY_CATAGORY_BY_PAGE_URL_API, requests.get, auth=AUTH)

class TestSubCatagory(testify.TestCase):
    """docstring for TestSubCatagory."""
    
    def test_unauth_search_subcatagory_url_api(self):
        return assert_url(SEARCH_BY_SUBCATAGORY_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_unauth_search_subcatagory_by_page_url_api(self):
        return assert_url(SEARCH_BY_SUBCATAGORY_BY_PAGE_URL_API, requests.get, code=UNAUTH_CODE)

    def test_auth_search_subcatagory_url_api(self):
        return assert_url(SEARCH_BY_SUBCATAGORY_URL_API, requests.get, auth=AUTH)
    
    def test_auth_search_subcatagory_by_page_url_api(self):
        return assert_url(SEARCH_BY_SUBCATAGORY_BY_PAGE_URL_API, requests.get, auth=AUTH)

class TestFilterBuild(testify.TestCase):
    """docstring for TestFilterBuild."""

    def test_unauth_search_build_url_api(self):
        return assert_url(SEARCH_BY_BUILD_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_unauth_search_build_by_page_url_api(self):
        return assert_url(SEARCH_BY_BUILD_BY_PAGE_URL_API, requests.get, code=UNAUTH_CODE)
        
    def test_auth_search_build_url_api(self):
        return assert_url(SEARCH_BY_BUILD_URL_API, requests.get, auth=AUTH)
    
    def test_auth_search_build_by_page_url_api(self):
        return assert_url(SEARCH_BY_BUILD_BY_PAGE_URL_API, requests.get, auth=AUTH)

class TestFilterLanguage(testify.TestCase):
    """docstring for TestFilterLanguage."""

    def test_auth_search_language_url_api(self):
        return assert_url(SEARCH_BY_LANGUAGE_URL_API, requests.get, auth=AUTH)
    
    def test_auth_search_language_by_page_url_api(self):
        return assert_url(SEARCH_BY_LANGUAGE_BY_PAGE_URL_API, requests.get, auth=AUTH)
        
    def test_unauth_search_language_url_api(self):
        return assert_url(SEARCH_BY_LANGUAGE_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_unauth_search_language_by_page_url_api(self):
        return assert_url(SEARCH_BY_LANGUAGE_BY_PAGE_URL_API, requests.get, code=UNAUTH_CODE)

class TestFilterPlatform(testify.TestCase):
    """docstring for TestFilterPlatform."""
    
    def test_unauth_search_platform_url_api(self):
        return assert_url(SEARCH_BY_PLATFORM_URL_API, requests.get, code=UNAUTH_CODE)

    def test_auth_search_platform_url_api(self):
        return assert_url(SEARCH_BY_PLATFORM_URL_API, requests.get, auth=AUTH)
    
    def test_auth_search_platform_by_page_url_api(self):
        return assert_url(SEARCH_BY_PLATFORM_BY_PAGE_URL_API, requests.get, auth=AUTH)
    
    def test_unauth_search_platform_by_page_url_api(self):
        return assert_url(SEARCH_BY_PLATFORM_BY_PAGE_URL_API, requests.get, code=UNAUTH_CODE)
        
class TestFilterTech(testify.TestCase):
    """docstring for TestFilterTech."""
        
    def test_unauth_search_tech_url_api(self):
        return assert_url(SEARCH_BY_TECH_URL_API, requests.get, code=UNAUTH_CODE)

    def test_auth_search_tech_url_api(self):
        return assert_url(SEARCH_BY_TECH_URL_API, requests.get, auth=AUTH)
    
    def test_unauth_search_tech_by_page_url_api(self):
        return assert_url(SEARCH_BY_TECH_BY_PAGE_URL_API, requests.get, code=UNAUTH_CODE)
    
    def test_auth_search_tech_by_page_url_api(self):
        return assert_url(SEARCH_BY_TECH_BY_PAGE_URL_API, requests.get, auth=AUTH)
    
if __name__ == '__main__':
    testify.run()
