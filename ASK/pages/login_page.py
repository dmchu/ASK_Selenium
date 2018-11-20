from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.params import DOMAIN
from parameters.parameters import *
from pages.base_page import BasePage

locators = {
    "login_email": {"by": By.ID, "locator": "mat-input-0"},
    "login_password": (By.ID, "mat-input-1"),
    "submit_button": (By.CSS_SELECTOR, "button[type='submit']"),
    "teacher_role_text": (By.XPATH, "// div[@class = 'info']/p[contains(text(),'TEACHER')]"),
    "student_role_text": (By.XPATH, "// div[@class = 'info']/p[contains(text(),'STUDENT')]")
}


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.page_url = DOMAIN + "/login"

    def login_as_teacher(self,email_teacher,password_teacher):
        driver = self.driver
        wait = self.wait
        driver.find_element(locators["login_email"]["by"], locators["login_email"]["locator"]).send_keys(email_teacher)
        driver.find_element(locators["login_password"][0], locators["login_password"][1]).send_keys(password_teacher)
        driver.find_element(locators["submit_button"][0], locators["submit_button"][1]).click()
        wait.until(EC.presence_of_element_located(locators["teacher_role_text"]))

    def login_as_student(self,email,password):
        driver = self.driver
        wait = self.wait
        driver.find_element(locators["login_email"]["by"], locators["login_email"]["locator"]).send_keys(email)
        driver.find_element(locators["login_password"][0], locators["login_password"][1]).send_keys(password)
        driver.find_element(locators["submit_button"][0], locators["submit_button"][1]).click()
        wait.until(EC.presence_of_element_located(locators["student_role_text"]))
