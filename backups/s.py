from selenium import webdriver
import time

#specify where your chrome driver present in your pc
PATH=r"C:\Users\educative\Documents\chromedriver\chromedriver.exe"
import undetected_chromedriver as uc
options = uc.ChromeOptions()
options.add_extension('AdBlock.crx')
#get instance of web driver
driver = uc.Chrome(use_subprocess=True,options=options)
driver.maximize_window()
#provide website url here
driver.get("https://omayo.blogspot.com/")

#sleep for 2 seconds
time.sleep(2)

#get button and click on it to get alert
driver.find_element("id","alert1").click()

#switch to alert box
alert = driver.switch_to.alert

#sleep for a second
time.sleep(1)

#accept the alert
alert.accept()