import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LaunchPage:
    email="//form[@role='form']//input[@id='email']"
    password = "//input[@id='password']"
    logbutton= "//input[@value='Login']"

    def __init__(self,driver):
            self.driver = driver

    def getemail(self):
        return self.driver.find_element(By.XPATH,self.email)


    def getpassword(self):
        return self.driver.find_element(By.XPATH, self.password)

    def getlogbutton(self):
        return self.driver.find_element(By.XPATH,self.logbutton)
    def enteremail(self,email):
        self.getemail().send_keys(email)

    def enterpassword(self,password):
        self.getpassword().send_keys(password)

    def clicklogbutton(self):
        self.getlogbutton().click()


