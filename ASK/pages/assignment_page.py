from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from fixtures.params import DOMAIN
from pages.base_page import BasePage
from parameters.parameters import *
from steps.common import click, type, wait_until

class AssignmentPage(BasePage):

    def __init__(self, driver):
        super(AssignmentPage, self).__init__(driver)
        self.page_url = DOMAIN + "/assignments"

    def create_new_assignment(self, quiz_name):
        click(self.driver, By.XPATH, "//span[contains(text(), 'Create New Assignment')]")
        wait_until(self.wait, self.driver, By.XPATH, "//span[contains(text(), 'Give Assignment')]")
        click(self.driver, By.XPATH, "//span[contains(text(), 'Select Quiz To Assign')]")
        wait_until(self.wait, self.driver, By.XPATH, "//mat-option[@class= 'mat-option ng-star-inserted mat-active']")
        # sleep(2)
        quiz_locator = "//mat-option/span[contains(text(),'{}')]".format(quiz_name)
        wait_until(self.wait, self.driver, By.XPATH, quiz_locator)
        element = self.driver.find_element_by_xpath(quiz_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        wait_until(self.wait, self.driver, By.XPATH, quiz_locator)
        student_locator = self.driver.find_element(By.XPATH, "//div[@class = 'mat-list-text']/*[contains(text(),'{}')]/..".format(student_id))
        self.driver.execute_script("arguments[0].scrollIntoView();", student_locator)
        student_locator.click()
        wait_until(self.wait, self.driver, By.XPATH, "//span[contains(text(), 'Give Assignment')]")
        click(self.driver,By.XPATH, "//span[contains(text(), 'Give Assignment')]")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "// mat-panel-title[contains(text(),'{}')]".format(quiz_name))))

