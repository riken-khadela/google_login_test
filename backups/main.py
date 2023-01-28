import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException,InvalidElementStateException
import time, random, pandas as pd
# class Main:
#   def __init_(self) -> None:
url    = 'https://accounts.google.com/ServiceLogin'

# options = uc.ChromeOptions()
# options.add_argument(f"--user-data-dir=/media/riken/0B29CA554279F37D/Workspace/google_login/profiles") 
# # options.headless = True
# options.add_argument(f'--profile-directory=Profile') 
# driver = uc.Chrome(use_subprocess=True,options=options)
# time   = 10
# driver.get("https://www.google.co.in")
# input('Enter')





# driver.get("https://www.google.co.in")
# input('Enter')
# driver.get("https://www.google.co.in")
# input('Enter')    
# driver.quit()


class driver:
    
    def __init__(self,email,password):
        self.profile_name = random.randint(100000,9999999)
        self.email = email
        self.password = password
        options = uc.ChromeOptions()
        options.add_argument(f"--user-data-dir=/media/riken/0B29CA554279F37D/Workspace/google_login/profiles") 
        # options.add_argument(f'--profile-directory=Profile') 
        # options.add_argument(f'--profile-directory=Profile 2') 
        options.add_argument(f'--profile-directory=Profile {self.profile_name}') 
        self.driver = uc.Chrome(use_subprocess=True,options=options)
        self.work()
    
    def find_element(self, element, locator, locator_type=By.XPATH,
            page=None, timeout=10,
            condition_func=EC.presence_of_element_located,
            condition_other_args=tuple()):
        """Find an element, then return it or None.
        If timeout is less than or requal zero, then just find.
        If it is more than zero, then wait for the element present.
        """
        try:
            if timeout > 0:
                wait_obj = WebDriverWait(self.driver, timeout)
                #  ele = wait_obj.until(
                #          EC.presence_of_element_located(
                #              (locator_type, locator)))
                ele = wait_obj.until(
                        condition_func((locator_type, locator),
                            *condition_other_args))
            else:
                print(f'Timeout is less or equal zero: {timeout}')
                ele = self.driver.find_element(by=locator_type,
                        value=locator)
            if page:
                print(
                        f'Found the element "{element}" in the page "{page}"')
            else:
                print(f'Found the element: {element}')
            return ele
        except (NoSuchElementException, TimeoutException) as e:
            if page:
                print(f'Cannot find the element "{element}"'
                        f' in the page "{page}"')
            else:
                print(f'Cannot find the element: {element}')
                
    def click_element(self, element, locator, locator_type=By.XPATH,
            timeout=10):
        """Find an element, then click and return it, or return None"""
        ele = self.find_element(element, locator, locator_type, timeout=timeout)
        if ele:
            ele.click()
            print(f'Clicked the element: {element}')
            return ele

    def input_text(self, text, element, locator, locator_type=By.XPATH,
            timeout=10, hide_keyboard=True):
        """Find an element, then input text and return it, or return None"""
        
        ele = self.find_element(element, locator, locator_type=locator_type,
                timeout=timeout)
        if ele:
            ele.clear()
            ele.send_keys(text)
            print(f'Inputed "{text}" for the element: {element}')
            return ele    
    
    def work(self):
        self.driver.get('https://facebook.com')
        self.driver.get("https://www.google.co.in")
        self.click_element('Sign in','//*[@id="gb"]/div/div[2]/a')
        
        # enter email
        self.input_text(self.email,'Email input','//*[@id="identifierId"]')
        self.click_element('Next','//*[@id="identifierNext"]/div/button')
        
        time.sleep(3)
        # enter password
        self.input_text(self.password,'password input','//*[@id="password"]/div[1]/div/div[1]/input')
        self.click_element('Next btn','//*[@id="passwordNext"]/div/button')
        
        
        
        input('Enter')
        self.driver.close()
        
        file_obj = open('accounts.csv', 'a')
        file_obj.write(f'{self.profile_name},{self.email},{self.password}\n')
        file_obj.close()
        
        

df = pd.read_csv('google_accounts_Sheet2.csv')
for i in range(len(df)):
    email = df.loc[i]['Email']
    password = df.loc[i]['Password']
    driver(email,password)
    
