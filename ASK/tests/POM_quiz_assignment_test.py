import unittest
from selenium.webdriver.common.by import By
from direct_commands.commands_with_api import *
from fixtures.base import BaseTestCase
from pages.assignment_page import AssignmentPage
from pages.login_page import LoginPage
from pages.my_assignments_page import MyAssignmentsPage
from pages.quiz_page import QuizPage
from pages.submission_page import SubmissionPage
from parameters.parameters import *


class QuizAssignmentTestCase(BaseTestCase):

    def setUp(self):
        super(QuizAssignmentTestCase, self).setUp()
        self.login_page = LoginPage(self.driver)
        self.login_page.goto_page()

    def tearDown(self):
        super(QuizAssignmentTestCase, self).tearDown()
        if self.assignment:
            delete_assignment_api(self, email_teacher, password_teacher, self.quiz_name)
        if self.quiz_name:
            delete_quiz_api(self, email_teacher, password_teacher, self.quiz_name)

        self.driver.quit()

    def test_quiz_assignment(self):
        # login_page.goto_page()
        driver = self.driver
        login_page = self.login_page
        # 1. Login as Teacher
        login_page.login_as_teacher(email_teacher, password_teacher)
        # 2. Create quiz
        quiz_page = QuizPage(driver)
        quiz_page.create_new_quizz(quiz_name)
        quiz_page.create_textual_question(textual_question_1)
        quiz_page.create_single_choice_question(single_choice_1, single_choice_1_opt_1,single_choice_1_opt_1, single_choice_1_opt_2)
        quiz_page.create_multiple_choice_question(multiple_choice_1, multiple_choice_1_opt_1, multiple_choice_1_opt_1, multiple_choice_1_opt_2)
        quiz_page.save_quiz(quiz_name)
        self.quiz_name = quiz_name
        # driver.get_screenshot_as_file('{} created.png'.format(self.quiz_name))
        # 3. go_to Assignment and create new assignment
        assignment_page = AssignmentPage(driver)
        assignment_page.goto_page()
        assignment_page.create_new_assignment(self.quiz_name)
        self.assignment = True
        assignment_page.logout()
        # log in as student
        login_page.login_as_student(email_student,password_student)
        # go_to my assignment
        my_assignments = MyAssignmentsPage(driver)
        my_assignments.goto_page()
        my_assignments.go_to_my_assignments()
        # answer quiz and submit my answer
        my_assignments.answer_quiz_and_submit(textual_question_1_answer)
        # log out as student
        login_page.logout()
        # log in as teacher
        login_page.login_as_teacher(email_teacher, password_teacher)
        # go to my submissions
        submission_page = SubmissionPage(driver)
        submission_page.goto_page()
        submission_page.grade_quiz(student_id,self.quiz_name)
        # verify that page loads
        result_label = "//div[@class = 'result']/div[contains(text(), 'ASSESSMENT')]"
        self.assertTrue(driver.find_element(By.XPATH, result_label))
        # driver.get_screenshot_as_file('Assignment for {} created.png'.format(self.quiz_name))
        login_page.logout()
        # delete_assignment_api(self, email_teacher, password_teacher, self.quiz_name)

if __name__ == '__main__':
    unittest.main()
