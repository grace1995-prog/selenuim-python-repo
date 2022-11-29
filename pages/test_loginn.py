import pytest
from ddt import ddt,data,unpack
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.yatra_launch_page import LaunchPage

@pytest.mark.usefixtures("setup")
@ddt
class Test_login():
    @data(("graceuko45@gmail.com","FR@2EvPgk2YnJN7"))
    @unpack
    def test_login(self):
        lp = LaunchPage(self.driver)
        lp.email("email")

        lp.password("password")

        lp.clickbutton()
