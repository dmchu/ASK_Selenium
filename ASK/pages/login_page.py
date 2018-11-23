from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.params import DOMAIN
from parameters.parameters import *
from pages.base_page import BasePage

locators = {
    "login_email": {"by": By.XPATH, "locator": "//input[@formcontrolname='email']"},
    "login_password": (By.XPATH, "//input[@type='password']"),
    "submit_button": (By.CSS_SELECTOR, "button[type='submit']"),
    "teacher_role_text": (By.XPATH, "// div[@class = 'info']/p[contains(text(),'TEACHER')]"),
    "student_role_text": (By.XPATH, "// div[@class = 'info']/p[contains(text(),'STUDENT')]")
}


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.page_url = DOMAIN + "/login"

    def login_as_teacher(self,email_teacher,password_teacher):
        self.driver.find_element(locators["login_email"]["by"], locators["login_email"]["locator"]).send_keys(email_teacher)
        self.driver.find_element(locators["login_password"][0], locators["login_password"][1]).send_keys(password_teacher)
        self.driver.find_element(locators["submit_button"][0], locators["submit_button"][1]).click()
        self.wait.until(EC.presence_of_element_located(locators["teacher_role_text"]))

    def login_as_student(self,email_student,password_student):
        self.driver.find_element(locators["login_email"]["by"], locators["login_email"]["locator"]).send_keys(email_student)
        self.driver.find_element(locators["login_password"][0], locators["login_password"][1]).send_keys(password_student)
        self.driver.find_element(locators["submit_button"][0], locators["submit_button"][1]).click()
        self.wait.until(EC.presence_of_element_located(locators["student_role_text"]))


