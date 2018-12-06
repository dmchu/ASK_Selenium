from time import sleep
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from fixtures.params import DOMAIN
from pages.base_page import BasePage

locators = {
    "forgot_password_email": {"by": By.XPATH, "locator": "//input[@placeholder='Email']"},
    "submit_button": (By.CSS_SELECTOR, "button[type='submit']"),
    "return_button": (By.XPATH, "//button[contains(@class,'mat-button')]"),
    "error_message": (By.XPATH, "//simple-snack-bar[contains(test(),'Failed')]")
}


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super(ForgotPasswordPage, self).__init__(driver)
        self.page_url = DOMAIN + "/forgot-password"
        self.actual_message = None

    def send_wrong_email(self,email):
        self.driver.find_element(locators["forgot_password_email"]["by"], locators["forgot_password_email"]["locator"]).send_keys(email)
        self.driver.find_element(locators["submit_button"][0], locators["submit_button"][1]).click()
        self.actual_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Authentication failed')]"))).text
        # self.wait.until(EC.presence_of_element_located(locators["teacher_role_text"]))

    def send_empty_email(self,email):
        self.driver.find_element(locators["forgot_password_email"]["by"], locators["forgot_password_email"]["locator"]).send_keys(email)
        self.driver.find_element(locators["submit_button"][0], locators["submit_button"][1]).click()
        self.actual_message = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//form//mat-error"))).text
        # self.wait.until(EC.presence_of_element_located(locators["teacher_role_text"]))

    def send_email_invalid(self,email):
        self.driver.find_element(locators["forgot_password_email"]["by"], locators["forgot_password_email"]["locator"]).send_keys(email)
        self.driver.find_element(locators["submit_button"][0], locators["submit_button"][1]).click()
        self.actual_message = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//form//mat-error"))).text
        # self.wait.until(EC.presence_of_element_located(locators["teacher_role_text"]))

    def send_valid_email(self,email):
        self.driver.find_element(locators["forgot_password_email"]["by"], locators["forgot_password_email"]["locator"]).send_keys(email)
        self.driver.find_element(locators["submit_button"][0], locators["submit_button"][1]).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text() ='Your request is confirmed']")))

    def reset_password(self,url):
        self.driver.get(url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.driver.find_element_by_xpath("//div[@id='email-table']//div[contains(text(),'assessment.portnov@gmail.com')]").click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn-primary")))
        reset_password_link = self.driver.find_element_by_css_selector("a.btn-primary").get_attribute('href')
        self.driver.get(reset_password_link)

    def change_password(self, password):
        self.driver.find_element_by_xpath("//form//mat-form-field[1]//input").click()
        self.driver.find_element_by_xpath("//form//mat-form-field[1]//input").send_keys(password)
        self.driver.find_element_by_xpath("//form//mat-form-field[2]//input").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h4[text() = 'Your Password was Changed']")))
        with open("/Users/RES/PycharmProjects/ASK_Selenium/ASK/parameters/parameters.py", 'r') as input_file, open(
                "/Users/RES/PycharmProjects/ASK_Selenium/ASK/parameters/parameters_new.py", 'w') as output_file:
            v_p = "val_password"
            for line in input_file:
                if v_p in line:
                    line = line.replace(line, "val_password = '{}'\n".format(password))
                    output_file.write(line)
                else:
                    output_file.write(line)
        os.rename('/Users/RES/PycharmProjects/ASK_Selenium/ASK/parameters/parameters_new.py',
                  '/Users/RES/PycharmProjects/ASK_Selenium/ASK/parameters/parameters.py')

    def change_password_with_existing(self, password):
        self.driver.find_element_by_xpath("//form//mat-form-field[1]//input").click()
        self.driver.find_element_by_xpath("//form//mat-form-field[1]//input").send_keys(password)
        self.driver.find_element_by_xpath("//form//mat-form-field[2]//input").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h4[text() = 'Your Password was Changed']")))


    def return_to_login(self):
        self.driver.find_element(locators["return_button"][0], locators["return_button"][1]).click()
        # self.wait.until(EC.presence_of_element_located(locators["student_role_text"]))


