import requests
import json


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
    self.assertTrue(r.status_code == 200)
    print("Quiz: {}  with id {} was permanently deleted".format(quiz_name, quiz_id))


def delete_assignment_api(self, email, password, quiz_name):

    url = "http://local.school.portnov.com:4520/api/v1/sign-in"

    payload = {
        'email': email,
        'password': password
    }

    headers = {
        'content-type': "application/json",
        'Connection': "keep-alive"
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    parsed_json = json.loads(r.text)

    token = parsed_json["token"]

    url = "http://local.school.portnov.com:4520/api/v1/assignments"

    headers = {
        'Authorization': "Bearer {}".format(token)
    }

    r = requests.get(url, headers=headers)

    parsed_json = json.loads(r.text)

    for i in parsed_json:
        if i['quiz']['name'] == quiz_name:
            assignment_group_id = i['assignmentGroupID']

            url = "http://local.school.portnov.com:4520/api/v1/assignment/{}".format(assignment_group_id)
            response = requests.delete(url, headers=headers)

            self.assertTrue(response.status_code == 200)
            print("Assignment: with {}  with id {} was permanently deleted".format(quiz_name, assignment_group_id))
        else:
            continue