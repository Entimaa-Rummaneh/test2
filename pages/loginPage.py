from selenium.webdriver.common.by import By
from pages.BasePage import BasePage



class LoginPage(BasePage):
    testbox_username_id = "USER_FULL_NAME"
    testbox_nationality_id = "ID_NUM"
    testbox_email_id="EMAIL"
    testbox_phone_id="CELULAR"
    button_accept_id= "registerCheck"
    buttonfollowing_xpath= "//span[contains(text(),'المتابعة')])[1]"

    def __init__(self, driver):
        super().__init__(driver)


    def setUserName(self, username):
        user_name_element = self.driver.find_element(By.ID, self.testbox_username_id)
        user_name_element.clear()
        user_name_element.send_keys(username)

    def setPassword(self, nationality):
        password_element = self.driver.find_element(By.ID, self.testbox_nationality_id)
        password_element.clear()
        password_element.send_keys(nationality)

    def setEmail(self, email):
        password_element = self.driver.find_element(By.ID, self.testbox_email_id)
        password_element.clear()
        password_element.send_keys(email)

    def setPhone(self, phone):
        password_element = self.driver.find_element(By.ID,self.testbox_phone_id)
        password_element.clear()
        password_element.send_keys(phone)

    def clickaccept(self):
        button = self.driver.find_element(By.ID, self.button_accept_id)
        button.click()

    def clickFollowing(self):
        button = self.driver.find_element(By.XPATH, self.buttonfollowing_xpath)
        button.click()