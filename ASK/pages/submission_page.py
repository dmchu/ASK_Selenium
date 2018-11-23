from time import sleep

from selenium.webdriver.common.by import By
from fixtures.params import DOMAIN
from pages.base_page import BasePage
from parameters.parameters import *
from steps.common import click, type, wait_until

class SubmissionPage(BasePage):

    def __init__(self, driver):
        super(SubmissionPage, self).__init__(driver)
        self.page_url = DOMAIN + "submissions/0"

    def grade_quiz(self, student_id, quiz_name):
        self.wait.until(self.EC.element_to_be_clickable((By.XPATH,
                                                         "//table//tr/td[contains(text(), '{}')]/../td[contains(text(),"
                                                         " '{}')]/..//button".format(student_id,quiz_name)))).click()
        wait_until(self.wait,self.driver,By.XPATH, "//div[@class = 'result']/div[contains(text(), 'ASSESSMENT')]")


