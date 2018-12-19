import os
import random

cwd = os.path.abspath(os.getcwd())
location_chrome = "../browsers/chromedriver"
location_firefox = "../browsers/geckodriver"

DOMAIN = "http://local.school.portnov.com:4520/#"
browsers = [
    "chrome",
    "firefox"
]
BROWSER_TYPE = random.choice(browsers)
CHROME_EXECUTABLE_PATH = os.path.join(cwd, location_chrome)
FIREFOX_EXECUTABLE_PATH = os.path.join(cwd, location_firefox)
EXPLICIT_TIMEOUT = 10
# Just example of some othe timeouts
# SLOW_TIMEOUT = 30
