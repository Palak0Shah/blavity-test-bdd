import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
# The driver.get method will navigate to a page given by the URL
# NOTE 1: This URL should reference localhost because it will run within a CircleCI container
# But to keep this example simple but informative, we are using an already deployed URL
# Check future posts for a complete code sample
driver.get("http://qxf2.com/selenium-tutorial-main")

# Create a screenshots directory if not present
# NOTE 2: We are taking screenshots to show CircleCI artifacts
if not (os.path.exists('./tests/screenshots')):
    os.makedirs('./tests/screenshots')
# Save screenshot in the created directory
driver.save_screenshot('./tests/screenshots/Qxf2_Tutorial_page.png')

# Assert the Page Title
assert "Qxf2 Services: Selenium training main" in driver.title9

# Close the browser window
driver.close()