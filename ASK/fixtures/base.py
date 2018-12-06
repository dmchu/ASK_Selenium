import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from direct_commands.commands_with_api import *

from fixtures.params import *
from pages.login_page import LoginPage
from parameters.parameters import *


class BaseTestCase(unittest.TestCase):
    def setUp(self):


        self.driver = webdriver.Chrome(executable_path="../browsers/chromedriver")
        # self.driver = webdriver.Firefox(executable_path="../browsers/geckodriver")
        # self.driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)

    def tearDown(self):
        self.driver.quit()


class TeacherLoginTestCase(BaseTestCase):
    def setUp(self):
        super(TeacherLoginTestCase, self).setUp()
        self.login = LoginPage(self.driver)
        self.login.goto_page()
        self.login.login_as_teacher(email_teacher, password_teacher)



if __name__ == '__main__':
    unittest.main()
