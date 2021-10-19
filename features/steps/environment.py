from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.headless = True
options.add_argument('--start-maximized')
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
options.binary_location = "ChromeExe/chromedriver_linux64/chromedriver"
user_agent = \
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 PTST/1.0'
options.add_argument('user-agent={0}'.format(user_agent))
# use this code below to execute headless state

# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
os.chmod('ChromeExe/chromedriver_linux64/chromedriver', 0o755)
print("Hi")
driver = webdriver.Chrome("ChromeExe/chromedriver_linux64/chromedriver",options=options)

# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(),options=options)

url_name = "https://staging.blavity.com/"

actions = ActionChains(driver)
