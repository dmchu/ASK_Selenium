from random import randint


# Test data:

# login_url = "http://local.school.portnov.com:4520/#/login"


email_teacher = 'alina.korolevich@yopmail.com'
password_teacher = 'internship'
user_role = "TEACHER"

email_student = 'talexandar@xumail.cf'



number = randint(100,1000)
quiz_name = "QA BASIC {}".format(number)
textual_question_1 = "What is Software Testing?"
textual_question_1_answer = 'Software Testing is the process of analyzing the software in order to detect differences between existing and required conditions and to evaluate the features of the software.'
textual_question_2 = "What is Software Quality Assurance?"
textual_question_3 = "Explain SDLC methodology?"

# Single choice questions:
single_choice_1 = "What is a Defect?"
single_choice_1_opt_1 = "Any flaw or imperfection in a software work product"
single_choice_1_answer = single_choice_1_opt_1
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
multiple_choice_1_answer = multiple_choice_1_opt_1
multiple_choice_2 = "Are Java and Javascript same languages?"
multiple_choice_2_opt_1 = "Yes"
multiple_choice_2_opt_2 = "No"
multiple_choice_3 = "What is a prime objective of a bug tracking database?"
multiple_choice_3_opt_1 = "Tracking the bugs"
multiple_choice_3_opt_2 = "To get a bug fixed"

# Forgot password:
email_not_in_database = "email@yopmail.com"
email_in_database = "vannihacoz-8337@yopmail.com"
empty_email = ''
email_invalid = 'abcd.com'
email_valid = "talexandar@xumail.cf"
url_valid_email = 'https://generator.email/talexandar@xumail.cf'
user_name = "Andrew Hoffman"
val_password = 'internship884'
new_valid_password = "internship{}".format(number)
student_id = 'a345'
