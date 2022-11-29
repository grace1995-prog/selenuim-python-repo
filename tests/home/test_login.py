import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.yatra_launch_page import LaunchPage

@pytest.mark.usefixtures("setup")
class Test_login():

    def test_login(self):
        lp = LaunchPage(self.driver)

        lp.enteremail("graceuko45@gmail.com")


        lp.enterpassword("FR@2EvPgk2YnJN7")



        lp.clicklogbutton()






