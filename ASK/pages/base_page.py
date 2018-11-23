from selenium.webdriver.support.wait import WebDriverWait
from steps.common import click, type, wait_until
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """ Class assigns all common functionality to other pages """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.page_url = None
        self.EC = EC

    def goto_page(self):
        self.driver.get(self.page_url)

    def logout(self):
        click(self.driver, By.XPATH, "//div[@class='mat-list-item-content']//h5[contains(text(),'Log Out')]")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mat-button.mat-warn")))
        click(self.driver, By.CSS_SELECTOR, ".mat-button.mat-warn")
        # self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(),'Register Now')]")))