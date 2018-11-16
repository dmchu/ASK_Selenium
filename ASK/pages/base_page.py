from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    """ Class assigns all common functionality to other pages """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.page_url = None

    def goto_page(self):
        self.driver.get(self.page_url)
