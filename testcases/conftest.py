import pytest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    # if browser == 'chrome':
    #     driver = webdriver.Chrome(service=Service('C:\webdrivers\chromedriver.exe'))
    #     print("Launching Chrome browser")
    # elif browser == 'firefox':
    #     driver = webdriver.firefox(service=Service('C:\webdrivers\geckodriver.exe'))
    #     print("Launching firefox browser")
    #driver = webdriver.Chrome(service=Service('C:\webdrivers\chromedriver.exe'))
    driver = webdriver.Edge(executable_path=r"C:\Users\Administrator\Downloads\driver\edgedriver_win64\msedgedriver.exe")
   # driver.get("https://istiqlalportal.fishost.net/register")
    #driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

