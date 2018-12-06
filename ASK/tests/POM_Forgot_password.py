import unittest
from fixtures.base import BaseTestCase
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from parameters.parameters import *

class ForgotPasswordTestCase(BaseTestCase):

    def setUp(self):
        super(ForgotPasswordTestCase, self).setUp()
        self.forgot_password_page = ForgotPasswordPage(self.driver)
        self.forgot_password_page.goto_page()
        self.login_page = LoginPage(self.driver)

    def test_user_email_do_not_exist_in_database(self):
        self.forgot_password_page.send_wrong_email(email_not_in_database)
        expected_message = 'Authentication failed. User not found or password does not match\nX'
        self.assertEqual(expected_message, self.forgot_password_page.actual_message)

    def test_user_email_required(self):
        self.forgot_password_page.send_empty_email(empty_email)
        expected_message = 'This field is required'
        self.assertEqual(expected_message, self.forgot_password_page.actual_message)

    def test_user_invalid_email(self):
        self.forgot_password_page.send_email_invalid(email_invalid)
        expected_message = 'Should be a valid email address'
        self.assertEqual(expected_message, self.forgot_password_page.actual_message)

    def test_user_valid_email(self):
        self.forgot_password_page.send_valid_email(email_valid)
        self.forgot_password_page.reset_password(url_valid_email)
        self.forgot_password_page.change_password(new_valid_password)
        self.login_page.goto_page()
        self.login_page.login(email_valid,new_valid_password)

    def test_user_old_password(self):
        self.forgot_password_page.send_valid_email(email_valid)
        self.forgot_password_page.reset_password(url_valid_email)
        self.forgot_password_page.change_password_with_existing(val_password)
        pass

if __name__ == '__main__':
    unittest.main()