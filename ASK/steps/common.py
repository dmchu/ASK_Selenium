from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import json


def type(driver, by, locator, text):
    element = driver.find_element(by,locator)
    element.clear()
    element.send_keys(text)


def click(driver, by, locator):
    element = driver.find_element(by, locator)
    element.click()


def wait_until(wait, driver, by, locator):
    wait.until(EC.visibility_of_element_located((by, locator)))


def login(driver, wait, login_url, email, password, role='TEACHER'):
    driver.get(login_url)
    type(driver, By.ID, "mat-input-0", email)
    type(driver, By.ID, "mat-input-1", password)
    click(driver, By.CSS_SELECTOR, "button[type='submit']")
    wait_until(wait, driver, By.XPATH, "// div[@class = 'info']/p[contains(text(),{})]".format(role))


def create_quizz_name(driver, wait, quiz_name):
    click(driver, By.PARTIAL_LINK_TEXT, "Quizzes")
    wait_until(wait, driver, By.CSS_SELECTOR, "a[href='#/quiz-builder']")
    click(driver, By.PARTIAL_LINK_TEXT, "Create New Quiz")
    type(driver, By.TAG_NAME, "input", quiz_name)


def add_new_question(driver, wait):
    by = By.CSS_SELECTOR
    locator = "div.controls.ng-star-inserted>button"
    wait_until(wait, driver, by, locator)
    click(driver, by, locator)


def create_textual_question(driver, wait, question):
    add_new_question(driver, wait)
    wait_until(wait, driver, By.CSS_SELECTOR, "div.left.wide mat-slider")
    text_type_locator = "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Textual')]"
    wait_until(wait, driver, By.XPATH, text_type_locator)
    click(driver, By.XPATH, text_type_locator)
    question_field_locator = "//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"
    wait_until(wait, driver, By.XPATH, question_field_locator)
    type(driver, By.XPATH, question_field_locator, question)


def create_single_choice_question(driver, wait, question, answer, *args):
    add_new_question(driver, wait)
    wait_until(wait, driver, By.CSS_SELECTOR, "div.left.wide mat-slider")
    single_choice_type_locator = "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Single-Choice')]"
    wait_until(wait, driver, By.XPATH, single_choice_type_locator)
    click(driver, By.XPATH, single_choice_type_locator)
    question_field_locator = "//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"
    wait_until(wait, driver, By.XPATH, question_field_locator)
    type(driver, By.XPATH, question_field_locator, question)
    for arg in args:
        wait_until(wait, driver, By.XPATH,
                   "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']".format(question,
                                                                                               args.index(arg) + 1))
        type(driver, By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']".format(question, args.index(arg) + 1), arg)
        if arg == answer:
            radio_button = "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']/../../../../..//mat-radio-button".format(question, args.index(arg)+1)
            click(driver, By.XPATH, radio_button)
        else:
            continue


def create_multiple_choice_question(driver, wait, question, answer, *args):
    add_new_question(driver, wait)
    multiple_choice_type_locator = "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Multiple-Choice')]"
    wait_until(wait, driver, By.XPATH, multiple_choice_type_locator)
    click(driver, By.XPATH, multiple_choice_type_locator)
    question_field_locator = "//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"
    wait_until(wait, driver, By.XPATH, question_field_locator)
    type(driver, By.XPATH, question_field_locator, question)
    for arg in args:
        wait_until(wait, driver, By.XPATH,
                   "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']".format(question,
                                                                                               args.index(arg) + 1))
        type(driver, By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']".format(question, args.index(arg) + 1), arg)
        if arg == answer:
            check_box = "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option {}*']/../../../../../mat-checkbox".format(question, args.index(arg)+1)
            click(driver, By.XPATH, check_box)
        else:
            continue


def save_quiz(driver, wait):
    by = By.XPATH
    save_btn = "//button/*[contains(text(),'Save')]"
    wait_until(wait, driver, by, save_btn)
    click(driver, by, save_btn)


def find_quizz(driver, wait, quiz_name):
    quiz_locator = "//ac-quizzes-list//div[@class = 'quizzes']//*[contains(text(),'{}')]".format(quiz_name)
    wait_until(wait, driver, By.XPATH, quiz_locator)
    element = driver.find_element_by_xpath(quiz_locator)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()


def logout(driver, wait):
    click(driver, By.XPATH, "//div[@class='mat-list-item-content']//h5[contains(text(),'Log Out')]")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mat-button.mat-warn")))
    click(driver, By.CSS_SELECTOR, ".mat-button.mat-warn")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[type='submit']")))


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
    print(r.status_code)
    self.assertTrue(r.status_code == 200)
    print("Quiz: {}  with id {} was permanently deleted".format(quiz_name, quiz_id))