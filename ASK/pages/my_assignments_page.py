from time import sleep

from selenium.webdriver.common.by import By
from fixtures.params import DOMAIN
from pages.base_page import BasePage
from parameters.parameters import *
from steps.common import click, type, wait_until


locators = {
    "assignment": (By.XPATH, "//td[contains(text(), '{}')]/../..//button".format(quiz_name)),
    "radio_button": (By.XPATH, "//div[@class='mat-radio-label-content'][contains(text(),'{}')]".format(single_choice_1_answer)),
    "check_box": (By.XPATH, "//mat-checkbox//*[contains(text(), '{}')]/..".format(multiple_choice_1_answer)),
    "student_role_text": (By.XPATH, "// div[@class = 'info']/p[contains(text(),'STUDENT')]")
}

class MyAssignmentsPage(BasePage):

    def __init__(self, driver):
        super(MyAssignmentsPage, self).__init__(driver)
        self.page_url = DOMAIN + "/my-assignments"

    def go_to_my_assignments(self):
        # self.driver.find_element(locators["submit_button"][0], locators["submit_button"][1]).click()
        # self.wait.until(self.EC.element_to_be_clickable((locators["assignment"][0],locators["assignment"][1]))).click()
        wait_until(self.wait,self.driver, locators["assignment"][0],locators["assignment"][1])
        self.driver.find_element(By.XPATH, "//td[contains(text(), '{}')]/../..//button".format(quiz_name)).click()
        wait_until(self.wait,self.driver,By.XPATH, '//textarea[@formcontrolname="textAnswer"]')

    def answer_quiz_and_submit(self, answer):
        self.driver.find_element(By.XPATH, '//textarea[@formcontrolname="textAnswer"]').send_keys(answer)
        self.wait.until(self.EC.element_to_be_clickable((locators["radio_button"][0], locators["radio_button"][1]))).click()
        self.wait.until(self.EC.presence_of_element_located((locators["check_box"][0], locators["check_box"][1]))).click()
        self.driver.find_element(By.XPATH, "//button/*[contains(text(), 'Submit My Answer')]").click()
        wait_until(self.wait,self.driver,By.XPATH,"//button[@aria-label = 'Close dialog']")
        self.driver.find_element(By.XPATH, "//button[@aria-label = 'Close dialog']").click()
        wait_until(self.wait,self.driver,By.XPATH, "//h4[contains(text(), 'My Assignments')]")


