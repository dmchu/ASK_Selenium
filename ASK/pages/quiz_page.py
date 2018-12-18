from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import json

from fixtures.params import DOMAIN
from pages.base_page import BasePage
from steps.common import click, type, wait_until



locators = {
    "create_quiz_btn": (By.XPATH, "//span[text() ='Create New Quiz']/.."),
    "quiz_name_field": (By.XPATH, "//label[contains(text(), 'Title Of The Quiz *')]/../../input"),
    "add_question_btn": (By.CSS_SELECTOR, "div.controls.ng-star-inserted>button"),
    "label_textual": (By.XPATH, "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Textual')]/.."),
    "label_single_choice": (By.XPATH, "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Single-Choice')]/.."),
    "label_multi_choice": (By.XPATH, "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Multiple-Choice')]/.."),
    "question_field_locator" : (By.XPATH, "//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"),
    "question_choice_field": (By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']"),
    "single_choice_radio_btn" : (By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']/../../../../..//mat-radio-button"),
    "multi_choice_ch_box" : (By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']/../../../../../mat-checkbox"),
    "save_quiz_btn" : (By.XPATH, "//button/*[contains(text(),'Save')]"),
    "quiz_locator" : (By.XPATH, "//ac-quizzes-list//div[@class = 'quizzes']//*[contains(text(),'{}')]")
}



class QuizPage(BasePage):

    def __init__(self, driver):
        super(QuizPage, self).__init__(driver)
        self.page_url = DOMAIN + "/quizzes"

    def create_new_quizz(self, quiz_name):
        self.wait.until(EC.element_to_be_clickable(
            (locators["create_quiz_btn"][0], locators["create_quiz_btn"][1]))).click()
        self.wait.until(EC.presence_of_element_located(
            (locators["quiz_name_field"][0], locators["quiz_name_field"][1]))).send_keys(quiz_name)

    def add_new_question(self):
        self.wait.until(EC.element_to_be_clickable(
            (locators["add_question_btn"][0], locators["add_question_btn"][1]))).click()
        self.wait.until(EC.element_to_be_clickable(
            (locators["add_question_btn"][0], locators["add_question_btn"][1])))

    def create_textual_question(self, question):
        self.add_new_question()
        self.wait.until(EC.element_to_be_clickable(
            (locators["label_textual"][0], locators["label_textual"][1]))).click()
        self.wait.until(EC.presence_of_element_located(
            (locators["question_field_locator"][0], locators["question_field_locator"][1]))).send_keys(question)

    def create_single_choice_question(self, question, answer, *args):
        self.add_new_question()
        self.wait.until(EC.element_to_be_clickable(
            (locators["label_single_choice"][0], locators["label_single_choice"][1]))).click()
        self.wait.until(EC.presence_of_element_located(
            (locators["question_field_locator"][0], locators["question_field_locator"][1]))).send_keys(question)
        for arg in args:
            self.wait.until(EC.visibility_of_element_located(
                (locators["question_choice_field"][0], locators["question_choice_field"][1].format(question, args.index(arg) + 1)))).send_keys(arg)
            if arg == answer:
                self.wait.until(EC.presence_of_element_located(
                    (locators["single_choice_radio_btn"][0], locators["single_choice_radio_btn"][1].format(question,args.index(arg) + 1)))).click()

    def create_multiple_choice_question(self, question, answer, *args):
        self.add_new_question()
        self.wait.until(EC.element_to_be_clickable(
            (locators["label_multi_choice"][0], locators["label_multi_choice"][1]))).click()
        self.wait.until(EC.presence_of_element_located(
            (locators["question_field_locator"][0], locators["question_field_locator"][1]))).send_keys(question)
        for arg in args:
            self.wait.until(EC.visibility_of_element_located(
                (locators["question_choice_field"][0],locators["question_choice_field"][1].format(question,args.index(arg) + 1)))).send_keys(arg)
            if arg == answer:
                self.wait.until(EC.presence_of_element_located(
                    (locators["multi_choice_ch_box"][0],locators["multi_choice_ch_box"][1].format(question,args.index(arg) + 1)))).click()

    def save_quiz(self, quiz_name):
        self.wait.until(EC.element_to_be_clickable(
            (locators["save_quiz_btn"][0], locators["save_quiz_btn"][1]))).click()
        self.wait.until(EC.presence_of_element_located(
            (locators["quiz_locator"][0], locators["quiz_locator"][1].format(quiz_name))))

    def find_quiz_in_list_of_quizzes(self, quiz_name):
        element = self.wait.until(EC.presence_of_element_located(
            (locators["quiz_locator"][0], locators["quiz_locator"][1].format(quiz_name))))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def get_screenshot(self, quiz_name):
        self.driver.get_screenshot_as_file('{} created.png'.format(quiz_name))

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
