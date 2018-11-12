import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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
from steps.common import click


class UserFirstNameTestSuit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../browsers/chromedriver")
        # self.driver = EventFiringWebDriver(webdriver.Chrome(executable_path="../browsers/chromedriver"), MyListener())
        #self.driver = webdriver.Firefox(executable_path="../browsers/geckodriver")
        self.wait = WebDriverWait(self.driver, 10)

    def test_first_name_alphanumerical_and_special_char(self):
        """ Verify that user can be created with 5 alphanumerical & special characters in First name """
        driver = self.driver
        wait = self.wait

        #test data
        first_name = "iV@#7"
        last_name = "Ivanov"
        email = "ivanobv@gmail.com"
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
        click()

        # Waits until new page loads
        back_to_login_page_btn = (By.XPATH, "//button/span[text()='Back to Login Page']")
        wait.until(EC.presence_of_element_located(back_to_login_page_btn))

        # Verify that successful message presents
        expected_confirm_msg = "You have been Registered."
        actual_confirm_msg = driver.find_element_by_css_selector(".mat-card > h4").text
        self.assertEqual(expected_confirm_msg, actual_confirm_msg)

        # entry = driver.get_log('browser')
        # for j, i in enumerate(entry):
        #     print(j + 1, "<", i["level"], ">", i["message"])

    def test_first_name_single_char(self):
        """ Verify that user can be created with single character in First name """

        # test data
        first_name = "i"
        last_name = "Ivanov"
        email = "ivanobv@gmail.com"
        group_id = "A007"
        password = "12345"
        confirm_password = "12345"

        driver = self.driver
        wait = self.wait
        # opens the registration page
        driver.get('http://local.school.portnov.com:4520/#/registration')

        # verify that page loads
        expected_title = 'Assessment Control @ Portnov'
        actual_title = driver.title
        self.assertEqual(expected_title, actual_title)

        # fill out registration form
        driver.find_element_by_id("mat-input-0").send_keys(first_name)
        driver.find_element_by_id("mat-input-1").send_keys(last_name)
        driver.find_element_by_id("mat-input-2").send_keys(email)
        driver.find_element_by_id("mat-input-3").send_keys(group_id)
        driver.find_element_by_id("mat-input-4").send_keys(password)
        driver.find_element_by_id("mat-input-5").send_keys(confirm_password)
        click()

        # Waits until new page loads
        back_to_login_page_btn = (By.XPATH, "//button/span[text()='Back to Login Page']")
        wait.until(EC.presence_of_element_located(back_to_login_page_btn))

        # Verify that successful message presents
        expected_confirm_msg = "You have been Registered."
        actual_confirm_msg = driver.find_element_by_css_selector(".mat-card > h4").text
        self.assertEqual(expected_confirm_msg, actual_confirm_msg)

    def test_first_name_zero_char(self):
        """ Verify that user can not create account with First name missing """

        # test data
        first_name = ""
        last_name = "Ivanov"
        email = "ivanobv@gmail.com"
        group_id = "A007"
        password = "12345"
        confirm_password = "12345"

        driver = self.driver
        wait = self.wait
        # opens the registration page
        driver.get('http://local.school.portnov.com:4520/#/registration')

        # verify that page loads
        expected_title = 'Assessment Control @ Portnov'
        actual_title = driver.title
        self.assertEqual(expected_title, actual_title)

        # fill out registration form
        driver.find_element_by_id("mat-input-0").send_keys(first_name)
        driver.find_element_by_id("mat-input-1").send_keys(last_name)
        driver.find_element_by_id("mat-input-2").send_keys(email)
        driver.find_element_by_id("mat-input-3").send_keys(group_id)
        driver.find_element_by_id("mat-input-4").send_keys(password)
        driver.find_element_by_id("mat-input-5").send_keys(confirm_password)
        click()

        # Verify that error message presents
        expected_error_msg = "This field is required"
        actual_error_msg = driver.find_element_by_xpath("//input[@id='mat-input-0']/../../..//mat-error").text
        self.assertEqual(expected_error_msg, actual_error_msg)


    def test_first_name_max_char(self):
        """ Verify that user can be created with 254 alphanumerical & special characters in First name """
        driver = self.driver
        wait = self.wait

        #test data
        first_name = "iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV" \
                     "@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#" \
                     "7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#"
        last_name = "I"
        email = "ivanobv@gmail.com"
        group_id = "A007"
        password = "12345"
        confirm_password = "12345"

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
        click()

        # Waits until new page loads
        back_to_login_page_btn = (By.XPATH, "//button/span[text()='Back to Login Page']")
        wait.until(EC.presence_of_element_located(back_to_login_page_btn))

        # Verify that successful message presents
        expected_confirm_msg = "You have been Registered."
        actual_confirm_msg = driver.find_element_by_css_selector(".mat-card > h4").text
        self.assertEqual(expected_confirm_msg, actual_confirm_msg)

    def test_first_name_max_character_plus_one(self):
        """ Verify that user can not create account with 254 plus one alphanumerical & special characters in First name """

        # test data
        first_name = "iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV" \
                     "@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#" \
                     "7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7iV@#7"
        last_name = "I"
        email = "ivanobv@gmail.com"
        group_id = "A007"
        password = "12345"
        confirm_password = "12345"

        driver = self.driver
        wait = self.wait
        # opens the registration page
        driver.get('http://local.school.portnov.com:4520/#/registration')

        # verify that page loads
        expected_title = 'Assessment Control @ Portnov'
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

        error = (By.XPATH, "//div[@class='cdk-global-overlay-wrapper']//simple-snack-bar")
        wait.until(EC.presence_of_element_located(error))
        # Verify that error message presents
        expected_error_msg = "Data too long for column 'name' at row 1\nX"
        actual_error_msg = driver.find_element_by_xpath("//div[@class='cdk-global-overlay-wrapper']//simple-snack-bar").text
        self.assertEqual(expected_error_msg, actual_error_msg)

    def test_first_name_leading_space(self):
        """ Verify that user can not create account with leading space in First name """

        # test data
        first_name = " Ivan"
        last_name = "Ivanov"
        email = "ivanobv@gmail.com"
        group_id = "A007"
        password = "12345"
        confirm_password = "12345"

        driver = self.driver
        wait = self.wait
        # opens the registration page
        driver.get('http://local.school.portnov.com:4520/#/registration')

        # verify that page loads
        expected_title = 'Assessment Control @ Portnov'
        actual_title = driver.title
        self.assertEqual(expected_title, actual_title)

        # fill out registration form
        driver.find_element_by_id("mat-input-0").send_keys(first_name)
        driver.find_element_by_id("mat-input-1").send_keys(last_name)
        driver.find_element_by_id("mat-input-2").send_keys(email)
        driver.find_element_by_id("mat-input-3").send_keys(group_id)
        driver.find_element_by_id("mat-input-4").send_keys(password)
        driver.find_element_by_id("mat-input-5").send_keys(confirm_password)
        click()

        # Verify that error message presents
        expected_error_msg = "Whitespaces are not allowed"
        actual_error_msg = driver.find_element_by_xpath("//input[@id='mat-input-0']/../../..//mat-error").text
        self.assertEqual(expected_error_msg, actual_error_msg)

    def test_first_name_trailing_space(self):
        """ Verify that user can not create account with trailing space in First name """

        # test data
        first_name = "Ivan "
        last_name = "Ivanov"
        email = "ivanobv@gmail.com"
        group_id = "A007"
        password = "12345"
        confirm_password = "12345"

        driver = self.driver
        wait = self.wait
        # opens the registration page
        driver.get('http://local.school.portnov.com:4520/#/registration')

        # verify that page loads
        expected_title = 'Assessment Control @ Portnov'
        actual_title = driver.title
        self.assertEqual(expected_title, actual_title)

        # fill out registration form
        driver.find_element_by_id("mat-input-0").send_keys(first_name)
        driver.find_element_by_id("mat-input-1").send_keys(last_name)
        driver.find_element_by_id("mat-input-2").send_keys(email)
        driver.find_element_by_id("mat-input-3").send_keys(group_id)
        driver.find_element_by_id("mat-input-4").send_keys(password)
        driver.find_element_by_id("mat-input-5").send_keys(confirm_password)
        click()

        # Verify that error message presents
        expected_error_msg = "Whitespaces are not allowed"
        actual_error_msg = driver.find_element_by_xpath("//input[@id='mat-input-0']/../../..//mat-error").text
        self.assertEqual(expected_error_msg, actual_error_msg)

    def test_first_name_space_character_inside(self):
        """ Verify that user can not create account with space character inside First name """

        # test data
        first_name = "Iv an"
        last_name = "Ivanov"
        email = "ivanobv@gmail.com"
        group_id = "A007"
        password = "12345"
        confirm_password = "12345"

        driver = self.driver
        wait = self.wait
        # opens the registration page
        driver.get('http://local.school.portnov.com:4520/#/registration')

        # verify that page loads
        expected_title = 'Assessment Control @ Portnov'
        actual_title = driver.title
        self.assertEqual(expected_title, actual_title)

        # fill out registration form
        driver.find_element_by_id("mat-input-0").send_keys(first_name)
        driver.find_element_by_id("mat-input-1").send_keys(last_name)
        driver.find_element_by_id("mat-input-2").send_keys(email)
        driver.find_element_by_id("mat-input-3").send_keys(group_id)
        driver.find_element_by_id("mat-input-4").send_keys(password)
        driver.find_element_by_id("mat-input-5").send_keys(confirm_password)
        click()

        # Verify that error message presents
        expected_error_msg = "Whitespaces are not allowed"
        actual_error_msg = driver.find_element_by_xpath("//input[@id='mat-input-0']/../../..//mat-error").text
        self.assertEqual(expected_error_msg, actual_error_msg)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
