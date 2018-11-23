import unittest
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import json
# from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
#
#
# class MyListener(AbstractEventListener):
#     def before_find(self, by, value, driver):
#         print(by, value)
#     def after_find(self, by, value, driver):
#         print(by, value, "found")
#     def on_exception(self, exception, driver):
#         print(exception)


class CreateQuizes(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../browsers/chromedriver")
        # self.driver = EventFiringWebDriver(webdriver.Chrome(executable_path="../browsers/chromedriver"), MyListener())
        #self.driver = webdriver.Firefox(executable_path="../browsers/geckodriver")
        self.wait = WebDriverWait(self.driver, 20)

    def test_create_quizes(self):
        """ Verify that user with Teachers role can Create Quiz with 3 Textual, 3 Single-Choice,
         3 Multiple-Choice questions 75% passing rate."""

        driver = self.driver
        wait = self.wait

        # Test data:
        number = randint(100,1000)
        quiz_name = "QA BASIC {}".format(number)
        textual_question_1 = "What is Software Testing?"
        textual_question_2 = "What is Software Quality Assurance?"
        textual_question_3 = "Explain SDLC methodology?"


        # 1. Login with tichers role

        email_teacher = 'alina.korolevich@yopmail.com'
        password_teacher = 'internship'

        login_url = "http://local.school.portnov.com:4520/#/login"
        driver.get(login_url)
        driver.find_element_by_id("mat-input-0").send_keys(email_teacher)
        driver.find_element_by_id("mat-input-1").send_keys(password_teacher)
        driver.find_element_by_css_selector("button[type='submit']").click()

        wait.until(EC.presence_of_element_located((By.XPATH, "// div[@class = 'info']/p[contains(text(),'TEACHER')]")))
        sleep(1)

        wait.until(EC.visibility_of_element_located((By.XPATH, "// div[@class = 'info']/p[contains(text(),'TEACHER')]")))
        driver.find_element(By.PARTIAL_LINK_TEXT, "Quizzes").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='#/quiz-builder']")))
        driver.find_element(By.PARTIAL_LINK_TEXT,"Create New Quiz").click()

        driver.find_element(By.TAG_NAME,"input").send_keys(quiz_name)

        driver.find_element(By.CSS_SELECTOR, "div.controls.ng-star-inserted>button").click()
        sleep(1)
        driver.find_element(By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Textual')]").click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div.mat-input-infix.mat-form-field-infix textarea").send_keys(textual_question_1)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div.controls.ng-star-inserted>button").click()
        sleep(1)
        driver.find_element(By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Textual')]").click()
        sleep(1)
        driver.find_element(By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']").send_keys(textual_question_2)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div.controls.ng-star-inserted>button").click()
        sleep(1)
        driver.find_element(By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Textual')]").click()
        sleep(1)
        driver.find_element(By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']").send_keys(textual_question_3)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div.controls.ng-star-inserted>button").click()
        sleep(1)

        # Single choice questions:
        single_choice_1 = "What is a Defect?"
        single_choice_1_opt_1 = "Any flaw or imperfection in a software work product"
        single_choice_1_opt_2 = "without any issues"
        single_choice_2 = "What is Priority?"
        single_choice_2_opt_1 = "It indicates the importance or urgency of fixing a defect"
        single_choice_2_opt_2 = "anytime can fix this bug. No time limit"
        single_choice_3 = "What is the difference between static testing?"
        single_choice_3_opt_1 = "without code executing the program is called as Static Testing."
        single_choice_3_opt_2 = "with code"

        driver.find_element(By.XPATH, "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Single-Choice')]").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']").send_keys(single_choice_1)
        sleep(1)
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 1*']".format(single_choice_1)).send_keys(single_choice_1_opt_1)
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 1*']/../../../../..//mat-radio-button".format(single_choice_1)).click()
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 2*']".format(single_choice_1)).send_keys(single_choice_1_opt_2)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div.controls.ng-star-inserted>button").click()
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.left.wide mat-slider")))
        driver.find_element(By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Single-Choice')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"))).send_keys(single_choice_2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 1*']".format(single_choice_2)))).send_keys(single_choice_2_opt_1)
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 1*']/../../../../..//mat-radio-button".format(single_choice_2)).click()
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 2*']".format(single_choice_2)).send_keys(single_choice_2_opt_2)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div.controls.ng-star-inserted>button").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.left.wide mat-slider")))
        driver.find_element(By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Single-Choice')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"))).send_keys(single_choice_3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 1*']".format(single_choice_3)))).send_keys(single_choice_3_opt_1)
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 1*']/../../../../..//mat-radio-button".format(single_choice_3)).click()
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 2*']".format(single_choice_3)).send_keys(single_choice_3_opt_2)


        # Multiple choice questions:
        multiple_choice_1 = "What is a Bug?"
        multiple_choice_1_opt_1 = "Mismatch between actual and intended behaviors of the software"
        multiple_choice_1_opt_2 = "Some small insect that flies around"
        multiple_choice_2 = "Are Java and Javascript same languages?"
        multiple_choice_2_opt_1 = "Yes"
        multiple_choice_2_opt_2 = "No"
        multiple_choice_3 = "What is a prime objective of a bug tracking database?"
        multiple_choice_3_opt_1 = "Tracking the bugs"
        multiple_choice_3_opt_2 = "To get a bug fixed"

        driver.find_element(By.CSS_SELECTOR, "div.controls.ng-star-inserted>button").click()
        driver.find_element(By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Multiple-Choice')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"))).send_keys(multiple_choice_1)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 1*']".format(multiple_choice_1)))).send_keys(multiple_choice_1_opt_1)
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 1*']/../../../../../mat-checkbox".format(multiple_choice_1)).click()
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 2*']".format(multiple_choice_1)).send_keys(multiple_choice_1_opt_2)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div.controls.ng-star-inserted>button").click()
        sleep(1)
        driver.find_element(By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Multiple-Choice')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"))).send_keys(multiple_choice_2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 1*']".format(multiple_choice_2)))).send_keys(multiple_choice_2_opt_1)
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 2*']".format(multiple_choice_2)).send_keys(multiple_choice_2_opt_2)
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 2*']/../../../../../mat-checkbox".format(multiple_choice_2)).click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div.controls.ng-star-inserted>button").click()
        sleep(1)
        driver.find_element(By.XPATH, "//*[contains(text(), 'new empty question')]/../../..//div[contains(text(), 'Multiple-Choice')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(), 'new empty question')]/../../..//textarea[@placeholder='Question *']"))).send_keys(multiple_choice_3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 1*']".format(multiple_choice_3)))).send_keys(multiple_choice_3_opt_1)
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 2*']".format(multiple_choice_3)).send_keys(multiple_choice_3_opt_2)
        driver.find_element(By.XPATH, "//*[contains(text(), '{}')]/../../..//*[@placeholder='Option 2*']/../../../../../mat-checkbox".format(multiple_choice_3)).click()

        driver.find_element(By.XPATH, "//button/*[contains(text(),'Save')]").click()
        quiz_locator = "//ac-quizzes-list//div[@class = 'quizzes']//*[contains(text(),'{}')]".format(quiz_name)
        wait.until(EC.visibility_of_element_located((By.XPATH, quiz_locator)))
        element = driver.find_element_by_xpath(quiz_locator)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        driver.get_screenshot_as_file('{} created.png'.format(quiz_name))
        driver.find_element_by_xpath("//div[@class='mat-list-item-content']//h5[contains(text(),'Log Out')]").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mat-button.mat-warn")))
        driver.find_element_by_css_selector(".mat-button.mat-warn").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[type='submit']")))


        #Sign in with role TEACHER

        email = 'alina.korolevich@yopmail.com'

        password = 'internship'

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

    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()
