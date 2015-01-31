from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# launch headless HTMLunit browser pointed at facebook
driver = webdriver.Remote("https://www.facebook.com", webdriver.DesiredCapabilities.HTMLUNITWITHJS)
