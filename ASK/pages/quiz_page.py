from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import json

from fixtures.params import DOMAIN
from pages.base_page import BasePage
from steps.common import click, type, wait_until

class QuizPage(BasePage):

    def __init__(self, driver):
        super(QuizPage, self).__init__(driver)
        self.page_url = DOMAIN + "/quizzes"

    def create_new_quizz(self, quiz_name):
        click(self.driver, By.PARTIAL_LINK_TEXT, "Quizzes")
        wait_until(self.wait, self.driver, By.CSS_SELECTOR, "a[href='#/quiz-builder']")
        click(self.driver, By.PARTIAL_LINK_TEXT, "Create New Quiz")
        type(self.driver, By.TAG_NAME, "input", quiz_name)
        self.quiz_name = quiz_name

    def add_new_question(self):
        by = By.CSS_SELECTOR
        locator = "div.controls.ng-star-inserted>button"
        wait_until(self.wait, self.driver, by, locator)
        click(self.driver, by, locator)

    def create_textual_question(self, question):
        self.add_new_question()
        wait_until(self.wait, self.driver, By.CSS_SELECTOR, "div.left.wide mat-slider")
        text_type_locator = "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Textual')]/.."
        self.wait.until(EC.element_to_be_clickable((By.XPATH, text_type_locator))).click()
        question_field_locator = "//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"
        wait_until(self.wait, self.driver, By.XPATH, question_field_locator)
        type(self.driver, By.XPATH, question_field_locator, question)

    def create_single_choice_question(self, question, answer, *args):
        self.add_new_question()
        wait_until(self.wait, self.driver, By.CSS_SELECTOR, "div.left.wide mat-slider")
        single_choice_type_locator = "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Single-Choice')]/.."
        self.wait.until(EC.element_to_be_clickable((By.XPATH, single_choice_type_locator))).click()
        question_field_locator = "//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"
        wait_until(self.wait, self.driver, By.XPATH, question_field_locator)
        type(self.driver, By.XPATH, question_field_locator, question)
        for arg in args:
            wait_until(self.wait, self.driver, By.XPATH,
                       "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']".format(question,
                                                                                                   args.index(arg) + 1))
            type(self.driver, By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']".format(question,
                                                                                                               args.index(
                                                                                                                   arg) + 1),
                 arg)
            if arg == answer:
                radio_button = "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']/../../../../..//mat-radio-button".format(
                    question, args.index(arg) + 1)
                click(self.driver, By.XPATH, radio_button)
            else:
                continue

    def create_multiple_choice_question(self, question, answer, *args):
        self.add_new_question()
        multiple_choice_type_locator = "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Multiple-Choice')]/.."
        self.wait.until(EC.element_to_be_clickable((By.XPATH, multiple_choice_type_locator))).click()
        question_field_locator = "//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"
        wait_until(self.wait, self.driver, By.XPATH, question_field_locator)
        type(self.driver, By.XPATH, question_field_locator, question)
        for arg in args:
            wait_until(self.wait, self.driver, By.XPATH,
                       "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']".format(question,
                                                                                                   args.index(arg) + 1))
            type(self.driver, By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']".format(question,
                                                                                                               args.index(
                                                                                                                   arg) + 1),
                 arg)
            if arg == answer:
                check_box = "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']/../../../../../mat-checkbox".format(
                    question, args.index(arg) + 1)
                click(self.driver, By.XPATH, check_box)
            else:
                continue

    def save_quiz(self, quiz_name):
        by = By.XPATH
        save_btn = "//button/*[contains(text(),'Save')]"
        wait_until(self.wait, self.driver, by, save_btn)
        click(self.driver, by, save_btn)
        quiz_locator = "//ac-quizzes-list//div[@class = 'quizzes']//*[contains(text(),'{}')]".format(quiz_name)
        wait_until(self.wait, self.driver, By.XPATH, quiz_locator)
        element = self.driver.find_element_by_xpath(quiz_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_quizz(self, quiz_name):

        quiz_locator = "//ac-quizzes-list//div[@class = 'quizzes']//*[contains(text(),'{}')]".format(quiz_name)
        wait_until(self.wait, self.driver, By.XPATH, quiz_locator)
        element = self.driver.find_element_by_xpath(quiz_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def logout(self):
        click(self.driver, By.XPATH, "//div[@class='mat-list-item-content']//h5[contains(text(),'Log Out')]")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mat-button.mat-warn")))
        click(self.driver, By.CSS_SELECTOR, ".mat-button.mat-warn")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    def delete_quiz_api(self, email, password, quiz_name):

        url = "http://local.school.portnov.com:4520/api/v1/sign-in"

        payload = {
            'email': email,
            'password': password
        }

        headers = {
            'content-type': "application/json",
            'Connection': "keep-alive"
        }

        response = requests.post(url, data=json.dumps(payload), headers=headers)

        parsed_json = json.loads(response.text)

        token = parsed_json["token"]

        url = "http://local.school.portnov.com:4520/api/v1/quizzes"

        headers = {
            'Authorization': "Bearer {}".format(token)
        }

        r = requests.get(url, headers=headers)
        parsed_json = json.loads(r.text)

        quiz_id = None

        for i in parsed_json:
            if i["name"] == quiz_name:
                quiz_id = i["id"]
            else:
                continue

        url = "http://local.school.portnov.com:4520/api/v1/quiz/{}".format(quiz_id)

        r = requests.delete(url, headers=headers)
        print("Status code:", r.status_code)
        self.driver.assertTrue(r.status_code == 200)
        print("Quiz: {}  with id {} was permanently deleted".format(quiz_name, quiz_id))
