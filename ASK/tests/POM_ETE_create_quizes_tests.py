import unittest
from fixtures.base import TeacherLoginTestCase
from parameters.parameters import *
from steps.common import *


class CreateQuizes(TeacherLoginTestCase):

    def setUp(self):
        super(CreateQuizes, self).setUp()
        # self.login_page = LoginPage(self.driver)
        # self.login_page.goto_page()

    def tearDown(self):
        super(CreateQuizes, self).tearDown()
        if self.quiz_name:
            delete_quiz_api(self, self.email_teacher, self.password_teacher, self.quiz_name)

    def test_create_quizes(self):
        """ Verify that user with Teachers role can Create Quiz with 3 Textual, 3 Single-Choice,
         3 Multiple-Choice questions 75% passing rate."""
        driver = self.driver
        wait = self.wait

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
        self.quiz_name = quiz_name
        self.email_teacher = email_teacher
        self.password_teacher = password_teacher

        find_quizz(driver, wait, quiz_name)
        driver.get_screenshot_as_file('{} created.png'.format(quiz_name))
        logout(driver, wait)


if __name__ == '__main__':
    unittest.main()
