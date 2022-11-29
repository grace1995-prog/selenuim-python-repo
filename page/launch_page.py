
from selenium.webdriver.common.by import By


class LaunchPage:

    def __init__(self, driver):
        self.driver = driver

    Email_Filed = "//form[@role='form']//input[@id='email']"
    def getEmail_Field(self):
        return self.driver.find_element(By.XPATH, "self.Email_field")
    def enterEmail_field(self,emailfield):
        self.getEmail_Field().send_keys(emailfield)

    #def email(self, email):
    #email = self.driver.find_element(By.XPATH, "//form[@role='form']//input[@id='email']").send_keys("email")

    #def password(self, password):
    #password = self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")

    #def button(self):
    #button = self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
