from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def fbupload(fileDir, email, pword):
        # launch headless PhantomJS browser pointed at facebook
        # https://stackoverflow.com/a/23872305

        # creates a new PhantomJS process
        #driver = webdriver.PhantomJS()
        driver = webdriver.Firefox()
        #email = "johaxworthless@gmail.com"
        #pword = "sbhacks15"

        driver.get('https://www.facebook.com')
        assert 'Facebook' in driver.title

        #https://stackoverflow.com/questions/25569426/unable-to-login-to-quora-using-selenium-webdriver-in-python
        form = driver.find_element_by_class_name("menu_login_container")
        username = form.find_element_by_name("email")
        username.send_keys(email)

        password = form.find_element_by_name("pass")
        password.send_keys(pword)
        password.send_keys(Keys.RETURN)

        assert 'Facebook' in driver.title

        driver.get('https://www.facebook.com/messages/' + '100009014106177')
        assert 'Messages' in driver.title
        f = open('messages.txt', 'w')
        f.write(str(driver.page_source.encode('utf-8')))
        f.close()
        #driver.save_screenshot('screenshot.jpg')

        tag = 'a._59hn'
        btns = driver.find_elements_by_css_selector(tag)
        links=open('links.txt','w')
        for btn in btns:
                links.write(btn.get_attribute('href')+'\n')
        links.close()
        input = driver.find_element_by_class_name("_3jk")
        attach = input.find_element_by_name("attachment[]")

        attach.send_keys(fileDir)

        message = driver.find_element_by_class_name("_1rt")
        m = message.find_element_by_name("message_body")
        m.send_keys(Keys.ENTER)
        #message[0].send_keys(Keys.ENTER)

        #wait = WebDriverWait(driver, 10)
        #table = wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, 'div._4-te'))

        #attach.send_keys(Keys.ENTER)
        #r = requests.post('https://www.facebook.com/ajax/bz')

        #driver.execute_script(\#$("js_3").click(function() {\
        #	var url = "ajax/bz";\
        #	var xhr = new XMLHttpRequest();
        #	xhr.open("POST", url, true);
        #	xhr.setRequestHeader("Content-Type", "application/x-javascript; charset=utf-8"
                
        #	\
        #});')
filedir='1.jpg'
username="johaxworthless@gmail.com"
password="sbhacks15"
fbupload(filedir,username,password)
