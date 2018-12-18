import unittest
from fixtures.base import TeacherLoginTestCase
from pages.quiz_page import QuizPage
from parameters.parameters import *
from steps.common import *

class CreateQuizes(TeacherLoginTestCase):

    def setUp(self):
        super(CreateQuizes, self).setUp()
        self.quiz = QuizPage(self.driver)

    def tearDown(self):
        super(CreateQuizes, self).tearDown()
        if self.quiz_name:
            delete_quiz_api(self, self.email_teacher, self.password_teacher, self.quiz_name)

    def test_create_quizes(self):
        """ Verify that user with Teachers role can Create Quiz with 3 Textual, 3 Single-Choice,
         3 Multiple-Choice questions 75% passing rate."""
        driver = self.driver
        wait = self.wait
        quiz = self.quiz

        quiz.goto_page()
        quiz.create_new_quizz(quiz_name)

        quiz.create_textual_question(textual_question_1)
        quiz.create_textual_question(textual_question_2)
        quiz.create_textual_question(textual_question_3)

        quiz.create_single_choice_question(single_choice_1,single_choice_1_opt_1,single_choice_1_opt_1,single_choice_1_opt_2)
        quiz.create_single_choice_question(single_choice_2,single_choice_2_opt_1,single_choice_2_opt_1,single_choice_2_opt_2)
        quiz.create_single_choice_question(single_choice_3,single_choice_3_opt_1,single_choice_3_opt_1,single_choice_3_opt_2)

        quiz.create_multiple_choice_question(multiple_choice_1,multiple_choice_1_opt_1,multiple_choice_1_opt_1,multiple_choice_1_opt_2)
        quiz.create_multiple_choice_question(multiple_choice_2,multiple_choice_2_opt_2,multiple_choice_2_opt_1,multiple_choice_2_opt_2)
        quiz.create_multiple_choice_question(multiple_choice_3,multiple_choice_3_opt_2,multiple_choice_3_opt_1,multiple_choice_3_opt_2)

        quiz.save_quiz(quiz_name)

        self.quiz_name = quiz_name
        self.email_teacher = email_teacher
        self.password_teacher = password_teacher

        quiz.find_quiz_in_list_of_quizzes(self.quiz_name)
        quiz.get_screenshot(self.quiz_name)


if __name__ == '__main__':
    unittest.main()
