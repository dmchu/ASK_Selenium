import unittest
from random import randint

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import login, create_quizz_name, create_textual_question, \
    create_single_choice_question, create_multiple_choice_question, save_quiz, find_quizz, logout, delete_quiz_api


class CreateQuizes(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../browsers/chromedriver")
        self.wait = WebDriverWait(self.driver, 20)


    def tearDown(self):
        self.driver.quit()



    def test_create_quizes(self):
        """ Verify that user with Teachers role can Create Quiz with 3 Textual, 3 Single-Choice,
         3 Multiple-Choice questions 75% passing rate."""

        driver = self.driver
        wait = self.wait

        # Test data:

        login_url = "http://local.school.portnov.com:4520/#/login"
        email_teacher = 'alina.korolevich@yopmail.com'
        password_teacher = 'internship'
        user_role = "TEACHER"

        number = randint(100,1000)
        quiz_name = "QA BASIC {}".format(number)
        textual_question_1 = "What is Software Testing?"
        textual_question_2 = "What is Software Quality Assurance?"
        textual_question_3 = "Explain SDLC methodology?"

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

        ################################### TEST #######################################

        login(driver, wait, login_url, email_teacher, password_teacher, user_role)
        create_quizz_name(driver, wait, quiz_name)

        create_textual_question(driver, wait, textual_question_1)
        create_textual_question(driver, wait, textual_question_2)
        create_textual_question(driver, wait, textual_question_3)

        create_single_choice_question(driver, wait, single_choice_1, single_choice_1_opt_1,single_choice_1_opt_1, single_choice_1_opt_2)
        create_single_choice_question(driver, wait, single_choice_2, single_choice_2_opt_1,single_choice_2_opt_1, single_choice_2_opt_2)
        create_single_choice_question(driver, wait, single_choice_3, single_choice_3_opt_1,single_choice_3_opt_1, single_choice_3_opt_2)

        create_multiple_choice_question(driver, wait, multiple_choice_1, multiple_choice_1_opt_1, multiple_choice_1_opt_1, multiple_choice_1_opt_2)
        create_multiple_choice_question(driver, wait, multiple_choice_2, multiple_choice_2_opt_2, multiple_choice_2_opt_1, multiple_choice_2_opt_2)
        create_multiple_choice_question(driver, wait, multiple_choice_3, multiple_choice_3_opt_2, multiple_choice_3_opt_1, multiple_choice_3_opt_2)

        save_quiz(driver, wait)
        find_quizz(driver, wait, quiz_name)
        driver.get_screenshot_as_file('{} created.png'.format(quiz_name))
        logout(driver, wait)
        delete_quiz_api(self, email_teacher,password_teacher,quiz_name)

if __name__ == '__main__':
    unittest.main()
