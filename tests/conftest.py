import pytest
from selenium import webdriver

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome("C:\\Users\\HP\\Downloads\\chromedriver_win32 (3)\\chromedriver.exe")

    baseURL = "https://courses.letskodeit.com/login"
    driver.get(baseURL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver




