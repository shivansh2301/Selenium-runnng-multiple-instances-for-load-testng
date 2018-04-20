from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
import random
import time
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
driver.get("http://localhost/dbmsproject_final_1/login_page.html")


r=random.randint(1,5)											#random wait to simulate user action
time.sleep(r)
#driver.implicitly_wait(r)

desig = driver.find_element_by_name("designation")
desig.send_keys('student')

usr = driver.find_element_by_name("username")
usr.send_keys(sys.argv[1])

passs = driver.find_element_by_name("password")
passs.send_keys(sys.argv[1])

passs.send_keys(Keys.RETURN)

driver.get("http://localhost/dbmsproject_final_1/submit_assignment.php?batch=IT6&course_code=CS1601")
cl = driver.find_element_by_name("clicker")
cl.click()

driver.find_element_by_name("file").send_keys(os.getcwd()+"/image.png")					#uploading a file


r=random.randint(1,5)
time.sleep(r)

driver.find_element_by_name("submit").click()


