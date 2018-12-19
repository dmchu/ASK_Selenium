
import unittest
from webbrowser import Error

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from fixtures.params import *
from pages.login_page import LoginPage
from parameters.parameters import *
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)
    def after_find(self, by, value, driver):
        print(by, value, "found")
    def on_exception(self, exception, driver):
        print(exception)


class BaseTestCase(unittest.TestCase):

    def get_browser(self):
        if BROWSER_TYPE.lower().find('chrome') >= 0:
            return webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        elif BROWSER_TYPE.lower().find('firefox') >= 0:
            return webdriver.Firefox(executable_path=FIREFOX_EXECUTABLE_PATH)
        else:
            raise Error('No such browser')


    def setUp(self):

        # self.driver = EventFiringWebDriver(webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH), MyListener())
        # self.driver = EventFiringWebDriver(self.get_browser(), MyListener())
        self.driver = self.get_browser()
        #self.driver = webdriver.Chrome(executable_path="../browsers/chromedriver")
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
