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

        # creates a new Firefox process
        #driver = webdriver.PhantomJS()
        driver = webdriver.Firefox()
        
        # TODO: read these in from user input
        email = "johaxworthless@gmail.com"
        pword = "sbhacks15"

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

		# TODO: determine user ID or username and subsitute
        driver.get('https://www.facebook.com/messages/' + '100009014106177')
        assert 'Messages' in driver.title
        #f = open('messages.txt', 'w')
        #f.write(str(driver.page_source.encode('utf-8')))
        #f.close()
        #driver.save_screenshot('screenshot.jpg')

        #tag = 'a._59hn'
        #btns = driver.find_elements_by_css_selector(tag)
        #links=open('links.txt','w')
        #for btn in btns:
        #        links.write(btn.get_attribute('href')+'\n')
        #links.close()
        
        input = driver.find_element_by_class_name("_3jk")
        attach = input.find_element_by_name("attachment[]")

        attach.send_keys(fileDir)

        message = driver.find_element_by_class_name("_1rt")
        m = message.find_element_by_name("message_body")
        m.send_keys(Keys.ENTER)
        #message[0].send_keys(Keys.ENTER)
        
def fbdownload(fileName, email, pword):
        # launch headless PhantomJS browser pointed at facebook
        # https://stackoverflow.com/a/23872305

        # creates a new PhantomJS process
        driver = webdriver.PhantomJS()
        #driver = webdriver.Firefox()
        
        # TODO: read these in from user input
        email = "johaxworthless@gmail.com"
        pword = "sbhacks15"

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

		# TODO: determine user ID or username and subsitute
        driver.get('https://www.facebook.com/messages/' + '100009014106177')
        assert 'Messages' in driver.title
        #f = open('messages.txt', 'w')
        #f.write(str(driver.page_source.encode('utf-8')))
        #f.close()
        #driver.save_screenshot('screenshot.jpg')

        tag = 'a._59hn'
        btns = driver.find_elements_by_css_selector(tag)
        #links=open('links.txt','w')
        urls = []
        
        # Append all result URLs to results
        for btn in btns:
			urls.append(btn.get_attribute('href'))
			
		# If URL matches filename, keep it in results
		results = filter(
					lambda match: re.search("\.txt\/" + fileName, match), urls)
		
		return sorted(results,
				key=lambda numerical: re.search(r'\.txt\/([^?]+)\?', numerical).group(1))
