import ddt as ddt
import pytest
from selenium import webdriver
from pages.loginPage import LoginPage



class TestLogin:
    baseURL = "https://istiqlalportal.fishost.net/register"
    username = "entimaa"
   # password = "momolove55M"
    nationality=40509983
    email="entimmarummaneh@gmail.com"
    phone=567154642

    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.nationality)
        self.lp.setEmail(self.email)
        self.lp.setPhone(self.phone)
        self.lp.clickaccept()
        self.lp.clickFollowing()
        self.driver.close()




