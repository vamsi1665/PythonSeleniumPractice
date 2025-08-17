import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("************** Test_001_Login *********** ")
        self.logger.info("************** verifing home page *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        act_title = self.driver.title
        if act_title=="nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** Home page passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********** Home page failed ***********")
            assert False

    def test_login(self,setup):
        self.logger.info("*********** verifing login test ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP=LoginPage(self.driver)
        self.LP.setUsername(self.username)
        self.LP.setPassword(self.password)
        self.LP.clicklogin()
        actual_title=self.driver.title
        if actual_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*********** verifing login test is passed ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshorts\\"+"test_login.png")
            self.driver.close()
            self.logger.error("*********** verifing login test is failed ***********")
            assert False



