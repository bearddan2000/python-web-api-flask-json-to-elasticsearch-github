from requests.auth import HTTPBasicAuth

AUTH = HTTPBasicAuth('user', 'pass')

UNAUTH_CODE = 401

URL = 'https://py-api-srv:443'

API = URL + "/api"

NAME_URL_API = API + '/name'

TOPIC_URL_API = API + '/topics'

CATAGORY_URL_API = API + '/catagory'

FILTER_URL_API = API + '/filter'

GET_ALL_URL_API = API + ''

GET_ALL_BY_PAGE_URL_API = API + '/2'

SEARCH_BY_NAME_URL_API = NAME_URL_API + '/java'

SEARCH_BY_NAME_BY_PAGE_URL_API = NAME_URL_API + '/2/java'

SEARCH_BY_TOPIC_URL_API = TOPIC_URL_API + '/java'

SEARCH_BY_TOPIC_BY_PAGE_URL_API = TOPIC_URL_API + '/2/java'

SEARCH_BY_CATAGORY_URL_API = CATAGORY_URL_API + '/programming'

SEARCH_BY_CATAGORY_BY_PAGE_URL_API = CATAGORY_URL_API + '/2/programming'

SEARCH_BY_SUBCATAGORY_URL_API = CATAGORY_URL_API + '/sub/test'

SEARCH_BY_SUBCATAGORY_BY_PAGE_URL_API = CATAGORY_URL_API + '/2/sub/test'

SEARCH_BY_BUILD_URL_API = FILTER_URL_API + '/build/maven'

SEARCH_BY_BUILD_BY_PAGE_URL_API = FILTER_URL_API + '/2/build/maven'

SEARCH_BY_LANGUAGE_URL_API = FILTER_URL_API + '/language/java'

SEARCH_BY_LANGUAGE_BY_PAGE_URL_API = FILTER_URL_API + '/2/language/java'

SEARCH_BY_PLATFORM_URL_API = FILTER_URL_API + '/platform/cli'

SEARCH_BY_PLATFORM_BY_PAGE_URL_API = FILTER_URL_API + '/2/platform/cli'

SEARCH_BY_TECH_URL_API = FILTER_URL_API + '/tech/bash'

SEARCH_BY_TECH_BY_PAGE_URL_API = FILTER_URL_API + '/2/tech/bash'

SMOKE_TEST_URL_API = API + '/smoke'