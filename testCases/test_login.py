import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        act_title = self.driver.title
        if act_title=="nopCommerce demo store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP=LoginPage(self.driver)
        self.LP.setUsername(self.username)
        self.LP.setPassword(self.password)
        self.LP.clicklogin()
        actual_title=self.driver.title

        if actual_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshorts\\"+"test_login.png")
            self.driver.close()
            assert False



