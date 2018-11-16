from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import click, type, wait_until

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 2)

    def login(self,login_url, email, password, role='TEACHER'):
        driver = self.driver
        wait = self.wait
        driver.get(login_url)
        type(driver, By.ID, "mat-input-0", email)
        type(driver, By.ID, "mat-input-1", password)
        click(driver, By.CSS_SELECTOR, "button[type='submit']")
        wait_until(wait, driver, By.XPATH, "// div[@class = 'info']/p[contains(text(),{})]".format(role))