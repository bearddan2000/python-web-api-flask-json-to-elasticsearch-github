from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import testify

SERVICE_URL = "https://py-web-srv:443/"

class TestSmoke(testify.TestCase):
    """docstring for TestSmoke."""

    def test_unauth_smoke_url(self):
        testify.assert_equal('Python', 'Python')

class TestGet(testify.TestCase):
    """docstring for TestGet."""

    @testify.setup
    def connect(self):
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities['acceptInsecureCert'] = True
        self.driver = webdriver.Remote("http://selenium:4444/wd/hub", capabilities)

    @testify.teardown
    def disconnect(self):
        self.driver.quit()

    def test_all_html(self):
        self.driver.get(SERVICE_URL)
        title = self.driver.title
        testify.assert_truthy('Python' in title)

    def test_all_html_by_page(self):
        self.driver.get(SERVICE_URL + "2")
        title = self.driver.title
        testify.assert_truthy('Python' in title)
    
    def test_search_by_name(self):
        self.driver.get(SERVICE_URL + "name/java")
        title = self.driver.title
        testify.assert_truthy('Python' in title)
    
    def test_search_by_name_page(self):
        self.driver.get(SERVICE_URL + "name/2/java")
        title = self.driver.title
        testify.assert_truthy('Python' in title)
    
if __name__ == '__main__':
    testify.run()
