import unittest
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
import json
import re
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


class ChangeUsersRoleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../browsers/chromedriver")
        # self.driver = EventFiringWebDriver(webdriver.Chrome(executable_path="../browsers/chromedriver"), MyListener())
        #self.driver = webdriver.Firefox(executable_path="../browsers/geckodriver")
        self.wait = WebDriverWait(self.driver, 10)

    def test_change_users_role(self):
        """ Verify that users role can be changed from STUDENT to TEACHER"""
        driver = self.driver
        wait = self.wait

        # 1.


        #test data
        first_name = "Appolon"
        last_name = "Jackson"
        email = "vsirlanovp8@korutbete.cf" #
        group_id = "A007"
        password = "12345"
        confirm_password = "12345"
        # TODO DC: May need to make separate file for parameters

        # opens the registration page
        driver.get('http://local.school.portnov.com:4520/#/registration')

        # verify that page loads
        expected_title='Assessment Control @ Portnov'
        actual_title = driver.title
        self.assertEqual(expected_title, actual_title)

        # fill out registration form
        driver.find_element_by_id("mat-input-0").send_keys(first_name)
        driver.find_element_by_id("mat-input-1").send_keys(last_name)
        driver.find_element_by_id("mat-input-2").send_keys(email)
        driver.find_element_by_id("mat-input-3").send_keys(group_id)
        driver.find_element_by_id("mat-input-4").send_keys(password)
        driver.find_element_by_id("mat-input-5").send_keys(confirm_password)
        driver.find_element_by_class_name("mat-raised-button").click()

        # Waits until new page loads
        back_to_login_page_btn = (By.XPATH, "//button/span[text()='Back to Login Page']")
        wait.until(EC.presence_of_element_located(back_to_login_page_btn))

        # Verify that successful message presents
        expected_confirm_msg = "You have been Registered."
        actual_confirm_msg = driver.find_element_by_css_selector(".mat-card > h4").text
        self.assertEqual(expected_confirm_msg, actual_confirm_msg)

        # Open email and copy registration link from confirmation letter

        url_email = "https://generator.email/vsirlanovp8@korutbete.cf"
        driver.get(url_email)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        driver.find_element_by_xpath("//div[@id = 'email-table']//div[contains(text(),'assessment.portnov@gmail.com')]").click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn-primary")))
        activation_link = driver.find_element_by_css_selector("a.btn-primary").get_attribute('href')

        # Confirm user using RESTAPI command

        user_id = activation_link.split("/")[-2]
        activation_token = activation_link.split("/")[-1]

        confirm_url = "http://local.school.portnov.com:4520/api/v1/activate/{}/{}".format(user_id,activation_token)

        response = requests.get(confirm_url)

        self.assertTrue(response.status_code == 200)



        # Sign in wtth role TEACHER

        email_teacher = 'alina.korolevich@yopmail.com'

        password_teacher = 'internship'

        login_url = "http://local.school.portnov.com:4520/#/login"
        driver.get(login_url)
        driver.find_element_by_id("mat-input-0").send_keys(email_teacher)
        driver.find_element_by_id("mat-input-1").send_keys(password_teacher)
        driver.find_element_by_css_selector("button[type='submit']").click()

        wait.until(EC.presence_of_element_located((By.XPATH,"// div[@class = 'info']/p[contains(text(),'TEACHER')]")))

        side_menu = driver.find_element_by_css_selector("ac-side-menu")
        side_menu.find_element_by_xpath('//h5[contains(text(),"User\'s Management")]').click()

        first_name = "Appolon"
        last_name = "Jackson"
        user_locator = "//mat-list-item//div[@class = 'mat-list-text']/h4[contains(text(),'{} {}')]".format(first_name,last_name)
        wait.until(EC.presence_of_element_located((By.XPATH, user_locator)))
        element = driver.find_element_by_xpath(user_locator)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mat-raised-button>span")))
        sleep(1)
        driver.get_screenshot_as_file('{} {} role before change.png'.format(first_name,last_name))
        driver.find_element_by_css_selector("button.mat-raised-button>span").click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="cdk-overlay-0"]/div/div/button[2][contains(text(),"")]')))
        sleep(1)
        driver.find_element_by_xpath('//*[@id="cdk-overlay-0"]/div/div/button[2][contains(text(),"")]').click()
        sleep(2)
        driver.find_element_by_xpath("// ac-modal-confirmation//button[@class='mat-button mat-warn']").click()
        sleep(1)
        driver.find_element_by_xpath("//div[@class='mat-list-item-content']//h5[contains(text(),'Log Out')]").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mat-button.mat-warn")))
        driver.find_element_by_css_selector(".mat-button.mat-warn").click()
        sleep(2)


        login_url = "http://local.school.portnov.com:4520/#/login"
        driver.get(login_url)
        email = "vsirlanovp8@korutbete.cf" #
        password = "12345"

        driver.find_element_by_css_selector("div>*[formcontrolname = 'email']").send_keys(email)
        driver.find_element_by_css_selector("div>*[formcontrolname = 'password']").send_keys(password)
        driver.find_element_by_css_selector("button[type='submit']").click()

        wait.until(EC.presence_of_element_located((By.XPATH, "// div[@class = 'info']/p[contains(text(),'TEACHER')]")))
        driver.get_screenshot_as_file('{} {} role after change.png'.format(first_name,last_name))
        actual_role = driver.find_element_by_xpath("// div[@class = 'info']/p").text
        self.assertEqual('TEACHER',actual_role)

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

        url = "http://local.school.portnov.com:4520/api/v1/users"

        headers = {
            'Authorization': "Bearer {}".format(token)
        }
        r = requests.get(url, headers=headers)
        parsed_json = json.loads(r.text)

        user_id = None

        for i in parsed_json:
            if i["email"] == "vsirlanovp8@korutbete.cf":
                user_id = i["id"]
            else:
                continue

        url = "http://local.school.portnov.com:4520/api/v1/users/{}".format(user_id)
        r = requests.delete(url, headers=headers)
        print(r.status_code)
        print("User: {} '{}' was permanently deleted".format(user_id, i["name"]))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
