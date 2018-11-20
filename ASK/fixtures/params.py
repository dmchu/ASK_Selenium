import os



cwd = os.path.abspath(os.getcwd())
location = "../browsers/chromedriver"

DOMAIN = "http://local.school.portnov.com:4520/#"
BROWSER_TYPE = "Chrome"
CHROME_EXECUTABLE_PATH = os.path.join(cwd, location)
EXPLICIT_TIMEOUT = 10
# Just example of some othe timeouts
# SLOW_TIMEOUT = 30
