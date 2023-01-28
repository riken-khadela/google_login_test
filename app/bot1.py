from django.core.management.base import BaseCommand
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException,InvalidElementStateException, ElementNotInteractableException
import time, random, pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from app.models import user
from selenium.webdriver.common.keys import Keys
import pyautogui, requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import os

ProxiesLi = ['51.15.242.202:8888','18.228.177.30:80','112.94.38.137:9002','103.152.112.145:80','47.243.121.74:3128','173.212.195.139:80','112.98.177.27:9091','195.113.244.81:3128','58.247.6.106:9002','103.117.192.14:80','213.135.235.227:80','118.27.113.167:8080','118.172.187.127:8080','103.151.30.81:8080','222.89.237.101:9002','103.99.249.209:80','180.168.113.227:9002','163.116.158.183:8081','110.52.103.74:9091','118.107.44.181:8000','117.160.132.37:9091','210.245.124.131:5239','198.58.100.137:3128','137.74.65.101:80','34.146.64.228:3128','43.255.113.232:82','80.169.156.52:8080','117.160.250.134:8081','146.190.231.87:3129','170.155.2.119:80','75.89.101.60:80','62.193.108.155:1976','129.213.95.20:80','116.203.153.165:80','195.8.249.242:80','123.54.16.53:9002','3.6.156.223:80','170.150.32.206:8080','121.52.71.23:80','178.253.236.139:8080','163.116.177.31:808','188.32.241.34:81','182.90.224.115:3128','58.246.58.150:9002','211.97.2.197:9002','196.203.30.85:8080','111.225.152.2:8089','177.93.50.106:999','163.116.248.40:808','54.209.104.192:3128','163.116.177.43:808','103.242.119.88:80','123.138.214.150:9002','218.204.162.123:9002','5.202.104.22:3128','35.202.186.72:80','113.208.119.142:9002','82.200.237.10:8080','23.94.98.201:8080','163.116.177.44:808','196.189.149.115:80','94.181.48.171:1256','117.54.114.100:80','47.176.62.178:3128','139.226.166.72:9002','154.85.58.149:80','178.128.199.145:80','91.224.168.22:8080','157.245.27.9:3128','58.20.248.139:9002','64.56.150.102:3128','117.160.250.138:81','138.186.63.138:80','43.204.16.38:80','80.211.23.121:80','60.246.239.213:80','47.95.254.71:80','168.181.196.76:8080','68.178.202.127:3128','117.139.124.182:9091','37.255.211.168:3128','140.206.62.198:9002','163.116.248.49:808','116.117.253.212:9002','37.59.250.103:80','114.143.242.234:80','119.196.168.205:80','163.116.248.53:808','43.251.135.19:8081','188.40.20.151:8000','123.157.233.138:9091','141.95.127.15:3128','110.12.211.140:80','202.200.170.238:80','120.197.157.44:9002','89.109.253.119:80','27.115.37.94:9002','178.62.92.133:80','159.138.139.32:8080','117.160.250.133:9999','178.212.54.137:8080','43.255.113.232:86','49.212.143.246:6666','120.236.74.213:9002','170.187.138.40:8009','103.134.177.158:8888','45.156.31.82:9090','118.107.44.181:80','103.87.201.185:80','20.110.99.169:80','143.198.228.250:80','109.207.76.37:8080','23.229.21.138:3128','117.160.250.134:9999','118.31.2.38:8999','82.165.190.65:80','180.168.191.195:9002','117.160.250.132:8080','94.130.177.190:9999','139.224.190.222:8083','195.8.249.243:80','128.199.202.122:8080','20.231.66.54:3128','51.68.181.108:80','163.116.177.51:808','174.139.41.164:9090','163.116.158.116:8081','5.180.181.26:8888','95.216.181.107:8128','197.245.230.122:41026','179.189.48.255:8080','41.65.236.37:1981','183.237.47.54:9091','154.118.228.212:80','182.237.16.7:83','39.107.33.254:8090','60.182.82.166:9002','93.188.161.84:80','167.71.5.83:8080','47.89.185.178:8888','124.156.100.83:8118','71.255.153.117:80','210.75.50.242:9002','146.56.119.252:80','109.111.8.7:8080','166.104.231.44:8888','104.223.135.178:10000','117.160.250.134:81','117.160.250.134:80','183.221.242.102:9443','91.245.73.117:8080','207.154.228.158:80','115.241.197.126:80','200.123.2.171:3128','82.121.212.126:80','109.68.145.110:3128','117.159.97.46:9002','123.130.152.2:9002','114.113.116.67:9091','178.32.101.200:80','118.185.179.10:80','35.221.104.58:3128','221.226.75.86:55443','117.160.250.134:8899','163.172.84.250:9741','62.193.108.146:1981','171.35.164.98:8085','110.240.50.48:9091','51.79.50.22:9300','185.106.113.51:80','116.113.68.130:9091','47.94.93.255:80','163.116.177.34:808','13.95.173.197:80','80.169.156.52:80','138.2.8.164:8000','3.226.168.144:80','120.236.64.75:9002','221.225.81.91:3128','220.87.121.155:80','103.163.51.254:80','51.15.20.159:3128','152.32.202.108:80','91.205.196.188:8080','155.133.26.123:8080','112.87.140.164:9401','120.197.161.66:9002','151.248.115.5:3128','117.160.250.133:80','5.134.216.58:8080','213.212.247.204:1976','183.64.239.19:8060','117.159.37.40:9091','163.116.177.45:808','41.65.227.103:1976','58.57.170.154:9002','163.116.158.115:8081','177.153.59.181:8080','163.116.158.25:8081','112.123.102.10:9002','163.116.248.42:808','112.120.41.71:80','45.5.118.43:999','120.82.174.128:9091','112.26.81.142:9091','90.45.141.107:80','58.222.193.162:2222','117.160.250.138:8081','91.212.124.55:80','221.231.23.53:9002','195.3.245.193:3128','111.43.105.50:9091','113.57.84.39:9091','159.192.249.98:8080','117.160.250.138:9999','162.62.81.27:81','139.255.74.124:8080','123.171.42.247:8089','110.164.15.182:8080','45.92.108.112:8080','80.169.156.52:443','176.192.70.58:8022','121.31.35.98:9091','188.40.20.151:8080','183.237.177.31:9091','111.225.152.216:8089','122.228.136.27:9091','222.139.221.185:9091','178.124.170.112:3128','163.116.158.117:8081','180.235.65.13:80','117.160.250.132:81','176.65.243.54:3128','223.210.2.228:9091','210.22.115.2:9002','154.236.184.86:1975','125.129.57.91:80','41.175.26.114:80','124.13.181.7:80','112.16.127.69:9002','163.116.158.26:8081','42.63.10.170:9002','60.2.153.186:9091','185.126.202.76:4005','112.133.231.132:8000','153.101.67.170:9002','88.8.167.19:80','217.6.28.219:80','41.65.236.56:1981','47.254.90.125:8008','163.116.158.114:8081','41.175.26.115:80','185.24.219.36:39811','163.116.177.46:808','4.233.217.172:80','136.243.134.87:80','109.194.22.61:8080','54.154.10.13:80','60.210.40.190:9091','119.197.92.165:80','222.98.194.210:80','43.255.113.232:80','112.103.198.145:9002','13.81.217.201:80','47.254.90.125:8888','81.69.172.135:80','220.248.70.237:9002','61.53.66.116:9091','117.160.250.132:8081','86.106.181.220:18379','193.3.20.13:80','161.117.89.36:8888','182.72.203.243:80','116.202.165.119:3124','109.207.105.200:6969','41.65.236.48:1976','163.116.177.39:808','190.5.77.211:80','120.237.142.198:9091','72.170.220.17:8080','116.203.201.82:8443','163.116.158.27:8081','47.74.152.29:8888','188.82.97.82:80','119.7.135.19:9091','51.158.154.173:3128','47.244.18.65:80','212.14.243.29:8080','171.35.164.81:8085','183.237.213.108:9002','112.87.140.163:9401','35.236.145.25:8090','167.99.131.11:80','173.249.198.244:8080','52.253.83.186:8090','117.160.250.138:8080','34.75.202.63:80','213.57.128.161:80','47.116.131.64:80','92.118.232.74:80','41.65.236.37:1976','27.115.74.26:9002','8.9.15.85:8090','20.210.26.214:3128','77.109.178.220:80','87.245.170.247:3128','216.137.184.253:80','154.236.168.179:1981','164.132.170.100:80','125.99.58.110:3128','117.160.250.132:80','117.159.10.124:9002','117.160.250.138:80','188.165.200.85:80','183.234.218.194:9002','102.38.14.177:8080','45.149.77.141:7000','3.214.57.254:80','117.158.173.216:9091','124.79.113.137:9002','20.187.77.5:80','195.110.59.82:80','218.7.171.91:3128','146.190.231.87:80','13.71.80.224:80','92.42.248.130:8888','103.78.97.38:8080','120.236.79.139:9002','163.116.158.23:8081','103.142.175.164:80','123.182.58.3:8089','195.154.255.194:8000','66.170.201.232:80','41.65.236.35:1981','78.38.93.152:3128','70.169.70.91:80','103.223.15.150:3128','117.160.250.133:8080','163.116.158.118:8081','116.121.74.66:80','62.3.41.234:8080','203.89.126.250:80','59.11.153.88:80','212.46.230.102:6969','101.52.251.186:8080','163.116.158.142:8081','117.160.250.134:82','194.31.150.253:80','61.220.170.133:8000','129.153.163.10:80','79.172.217.106:80','84.248.34.9:80','46.225.237.146:3128','149.34.3.152:8080','163.116.177.42:808','120.236.74.212:9002','112.120.127.146:80','43.255.113.232:85','146.190.123.209:80','171.34.53.2:9091','117.160.250.134:8080','213.188.155.41:80','46.47.197.210:3128','213.212.247.204:1981','120.197.219.82:9091','156.200.116.71:1981','43.255.113.232:8085','51.75.141.46:80','78.46.175.184:80','116.49.163.71:80','183.164.245.252:8089','61.7.146.7:8082','42.228.61.245:9091','185.37.24.242:80','78.47.68.183:80','74.208.51.197:5000','103.172.70.87:8080','103.149.130.38:80','47.254.90.125:8000','117.160.250.133:82','43.255.113.232:8084','163.116.177.32:808','163.116.177.50:808','120.237.144.200:9091','112.245.48.74:9002','87.255.6.218:8080','121.204.148.136:9002','163.116.158.28:8081','41.33.137.12:1981','46.101.126.180:42385','106.227.48.205:9002','124.13.181.6:80','61.178.141.146:80','47.99.96.187:80','58.152.47.105:80','103.154.230.82:5678','47.98.219.185:8999','101.200.220.107:8080','176.168.127.74:80','41.65.236.48:1981','101.226.17.188:9002','45.170.252.116:3128','80.53.244.214:42462','194.169.167.5:8080','47.243.167.229:80','113.195.3.153:8085','24.230.33.96:3128','41.175.26.113:80','163.116.177.47:808','62.193.110.132:1976','111.21.183.58:9091','43.255.113.232:8081','111.8.226.107:9091','106.14.255.124:80','34.239.204.118:80','221.6.139.190:9002','113.125.58.199:3128','122.5.23.14:9002','111.160.204.146:9091','205.185.126.246:3128','118.26.110.48:8080','1.116.202.121:80','106.83.197.83:9091','116.234.209.15:9002','212.182.90.118:80','47.243.180.142:808','182.253.109.83:8080','222.247.57.67:9002','112.5.56.2:9091','45.70.236.194:999','124.90.193.52:8085','117.160.250.133:81','117.159.70.77:9091','123.182.58.29:8089','163.116.158.143:8081','47.254.90.125:80','163.116.248.41:808','45.118.139.196:80','117.160.250.132:82','183.239.188.250:9002','103.77.60.14:80','116.202.165.119:3121','120.234.142.253:9002','185.20.198.250:8080','146.19.217.237:3128','207.154.230.195:8888','218.201.71.75:8060','222.234.220.170:3128','144.217.240.185:9300','183.239.62.59:9091','202.0.103.115:80','125.130.100.49:80','36.34.244.130:9091','14.139.242.7:80','101.226.17.48:9002','154.236.168.169:1976','101.68.17.124:8085','20.219.137.240:3000','163.116.248.47:808','180.164.58.37:9002','162.19.50.37:80','58.57.170.146:9002','122.116.150.2:9000','117.160.250.132:9999','41.65.236.57:1976','111.225.153.7:8089','178.121.130.27:9002','54.173.137.254:8090','103.122.90.254:80','47.90.126.138:9090','103.99.249.212:80','163.116.177.48:808','183.221.242.103:9443','104.45.128.122:80','103.99.249.211:80','205.215.16.189:80','58.253.210.122:8888','185.39.50.2:1337','103.150.18.218:80','173.212.200.30:3128','183.237.213.101:9002','120.236.69.185:9002','58.20.235.231:9002','122.252.182.122:53281','74.82.50.155:3128','3.220.186.248:80','52.53.251.113:3128','123.183.162.9:9002','183.237.211.10:9002','62.225.13.118:80','117.40.176.42:9091','104.211.204.88:80','221.178.242.90:9091','103.127.1.130:80','78.38.93.20:3128','60.198.53.23:80','46.160.245.209:82','195.154.114.49:8123','59.48.94.90:9091','156.200.116.68:1981','61.79.139.30:80','41.175.26.112:80','121.128.194.154:80','121.22.53.166:9091','221.193.240.115:9091','102.68.85.187:80','117.160.250.138:82','222.180.240.62:9091','95.183.232.220:80','93.240.114.68:4003','183.237.217.58:9002','43.255.113.232:84','188.40.20.151:3128','117.160.250.133:8081','223.112.174.62:9091','103.167.134.31:80','36.99.165.148:9002','159.138.158.36:8888','163.116.177.49:808','89.132.144.41:9090','103.43.151.36:80','120.236.89.166:9002','113.143.37.82:9002','8.210.52.87:8080','81.22.190.38:80','43.251.135.19:8080','172.177.221.87:80','178.54.21.203:8081','103.181.45.9:80','121.1.41.162:111','212.89.188.115:21231','5.102.71.22:8080','128.65.178.46:8080','89.43.10.141:80','223.113.80.158:9091','45.231.170.137:999','163.116.177.33:808','123.130.115.217:9091','91.142.90.220:3000','38.91.120.190:80','196.15.213.235:3128','113.57.109.37:8085','103.134.177.182:8888','109.238.181.53:8083','200.13.22.210:80','123.182.59.97:8089','182.106.220.252:9091','163.116.177.30:808','181.143.191.138:999','134.238.252.143:8080','103.99.249.210:80','112.194.142.135:9091','103.197.251.202:80','105.112.191.250:3128','154.236.177.117:1976','128.201.232.102:888','106.227.51.67:9002','198.49.68.80:80','155.185.245.110:80','111.225.152.156:8089','183.220.6.198:9091','120.234.135.251:9002','103.254.185.195:53281','123.182.59.67:8089','94.60.119.233:80','103.83.232.122:80','59.92.70.176:3127','85.246.73.46:80','181.129.251.147:8080','171.233.151.214:55443','41.77.188.131:80','116.98.229.22:10003','114.233.70.231:9000','120.34.241.162:8089','103.17.182.14:9191','2.188.166.22:3128','41.59.85.217:3128','103.118.175.220:80']

class YoutubeBot:
    def __init__(self):
        self.VideoDuration = ''
            
    def get_driver(self,email,password,profile_name,ChannelName,VideoTItle):
        proxy = random.choice(ProxiesLi)
        self.user = user.objects.get(email=email)
        self.ProfileDict = self.user.ProfileDict
        self.VideoTItle = VideoTItle
        self.ChannelName = ChannelName
        self.profile_name = profile_name
        self.email = email
        self.password = password
        print(self.ProfileDict,self.profile_name,self.email,self.password)   
        self.options = uc.ChromeOptions()
        self.options.add_argument(f"--user-data-dir=profiles{self.ProfileDict}") 
        # self.options.add_argument(f"--user-data-dir=profiles10") 
        self.options.add_argument(f'--profile-directory={self.profile_name}') 
        self.options.add_argument(f'--disable-dev-shm-usage') 
        # self.options.add_argument(f'--proxy-server={proxy_type}://{proxy}')
        # self.options.add_argument('--proxy-server=%s' % proxy)
        self.driver = uc.Chrome(use_subprocess=True,options=self.options)
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
        self.driver.maximize_window()
        self.driver.get('https://myaccount.google.com/')
        check_account = self.find_element('check account','/html/body/header/div[1]/div[5]/ul/li[2]/a',timeout=5)
        if check_account : 
            if check_account.text == 'Go to Google Account': 
                account_added = self.add_accounts()
                if account_added == False: return False
                
        # breakpoint()
        return self.driver
        
        
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
            for i in range(3):
                try: 
                    ele.send_keys(text)
                    print(f'Inputed "{text}" for the element: {element}')
                    return ele    
                except ElementNotInteractableException :...
    
    def check_proxy(self,category, agent, proxy, proxy_type='http'):
        if category == 'f':
            headers = {
                'User-Agent': f'{agent}',
            }

            proxy_dict = {
                "http": f"{proxy_type}://{proxy}",
                "https": f"{proxy_type}://{proxy}",
            }
            response = requests.get(
                'https://www.youtube.com/', headers=headers, proxies=proxy_dict, timeout=30)
            status = response.status_code

        else:
            status = 200

        return status
    
    def ScrollDown(self,px):
        self.driver.execute_script(f"window.scrollTo(0, {px})")
    
    def add_accounts(self):
        try: 
            self.driver.get('https://facebook.com')
            self.driver.get("https://www.google.com/intl/en-GB/gmail/about")
            time.sleep(random.randint(2,4))
            self.click_element('Sign in','/html/body/header/div/div/div/a[2]')
            
            # enter email
            Email_input = self.input_text(self.email,'Email input','//*[@id="identifierId"]')
            if Email_input :
                time.sleep(random.randint(2,4))
                self.click_element('Next','//*[@id="identifierNext"]/div/button')
                
                # enter password
                time.sleep(random.randint(2,4))
                self.input_text(self.password,'password input','//*[@id="password"]/div[1]/div/div[1]/input')
                time.sleep(random.randint(2,4))
                self.click_element('Next btn','//*[@id="passwordNext"]/div/button')
                time.sleep(random.randint(2,4))
                # not now btn
                self.click_element('Not now','//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[4]/div[1]/button')
            
                print('sucessfully email done')
                time.sleep(random.randint(2,4))
                try:
                    self.driver.find_element(By.XPATH,'//*[@id="gb"]/div[2]/div[3]/div[1]/div[2]/div/a/img')
                    return True
                except Exception as e:...   

        except Exception as e:...
        return False
    
    def engagement(self,video='',channel='',like=False,comment='',view=False, subscribe_video = False):
        self.driver.get('https://www.youtube.com/')
        count = 0
        if channel : self.subscribe_channel(channel)
        
        if video : 
            for i in range(2,7):
                # self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.COMMAND + 't')
                # time.sleep(5)
                # self.driver.find_element(By.XPATH,'/html/body').send_keys(Keys.CONTROL + 't')
                # self.driver.get('http://stackoverflow.com/')
                count+=1
                self.driver.window_new()
                for _ in range(2):
                    ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
                    self.driver.execute_script(f'window.open ("{video}" , "tab{i}")')
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    self.driver.get(video)
                    time.sleep(4)
                        
        if comment : self.CommentOnCurrentVideo(comment)
        
        if like : self.LikeOnCurrentVideo()
        time.sleep(40)
        self.CloseDriver()
        return count
        
    def random_engagement(self,video='',action='',title='',comment='',view=False, subscribe_video = False,channel='',like=False,channel_username='',VideoId=''):
        print('started random action @')
        if not (video or action) : 
            print('Please provide video link and action type')
            return 
        
        if action == "Search" :
            self.driver.get(f'https://www.youtube.com')
            self.type_keyword()
            self.get_videosbyTitle(title=self.VideoTItle)
            self.Video_action(comment=comment,view=view,subscribe_video=subscribe_video,channel=channel,like=like)
                            
        if action == 'GoogleSearch' :
            self.GoogleBrowseVideo()
            self.Video_action(comment=comment,view=view,subscribe_video=subscribe_video,channel=channel,like=like)
        
        if action == 'YahooSearch' :
            self.YahooBrowseVideo(VideoId=VideoId)
            self.Video_action(comment=comment,view=view,subscribe_video=subscribe_video,channel=channel,like=like)
                
        if action == 'HomeSuggestion':
            self.subscribe_channel(link=channel)
            self.OpenSuggestedVideo()
            self.Video_action(comment=comment,view=view,subscribe_video=subscribe_video,channel=channel,like=like)
                
        if action == 'ChannelPage':
            self.FindVideOnChannel(channel,channel_username)
            self.Video_action(comment=comment,view=view,subscribe_video=subscribe_video,channel=channel,like=like)
                
        if action == "DirectLink" :
            self.driver.get(video)
            self.Video_action(comment=comment,view=view,subscribe_video=subscribe_video,channel=channel,like=like)
        return 0
    
    def type_keyword(self):
        input_keyword = self.driver.find_element(By.CSS_SELECTOR, 'input#search')
        for letter in self.VideoTItle:
            input_keyword.send_keys(letter)
            time.sleep(random.uniform(.1, .4))
        self.driver.find_element(By.XPATH,'//*[@id="search-icon-legacy"]/yt-icon').click()
    
    def FindVideOnChannel(self,channelLink='',channel_username=''):
        if not channelLink : print('please provide valid channel link');return 
        self.driver.get(channelLink)
        
        self.driver.get(f'https://www.youtube.com/@{channel_username}/search?query={self.VideoTItle}')
        self.find_element('videos','ytd-item-section-renderer',By.TAG_NAME)
        allvideos = self.driver.find_elements(By.TAG_NAME,'ytd-item-section-renderer')
        for video in allvideos:
            VideoTitle = video.find_element(By.XPATH,'//div[3]/ytd-video-renderer/div[1]/div/div[1]/div/h3/a')
            if self.VideoTItle in VideoTitle.text:
                VideoTitle.click()
                return
        
    def OpenSuggestedVideo(self):
        time.sleep(random.randint(5,10))
        self.driver.get('https://youtube.com')
        self.find_element('grid','ytd-rich-grid-row',By.TAG_NAME,timeout=20)
        while True:
            VideoGrid = self.driver.find_elements(By.TAG_NAME,'ytd-rich-grid-row')
            for grid in VideoGrid:
                VideoEle = grid.find_elements(By.TAG_NAME,'ytd-rich-item-renderer')
                for Video in VideoEle:
                    title = Video.find_elements(By.ID,'video-title-link')
                    if title:
                        if self.VideoTItle in title[0].text:
                            title[0].click()
                            return

            self.find_element('Body','body',By.TAG_NAME).send_keys(Keys.CONTROL, Keys.END)
            time.sleep(random.randint(4,8))
        ...
    
    def GoogleBrowseVideo(self):
        self.driver.get('https://google.com')
        input = self.input_text(f'youtube {self.ChannelName} {self.VideoTItle}','Search input','gLFyf',By.CLASS_NAME)
        input.submit()
        self.find_element('Google search result','MjjYud',By.CLASS_NAME)
        video = self.click_element('Browsed Video','//*[@id="rso"]/div[1]/div/div/div/video-voyager/div/div[1]/div[1]/a')
        if video : return
        
    def YahooBrowseVideo(self,VideoId=''):
        
        link = 'https://search.yahoo.com/'
        print('Search in Yahoo')
        self.driver.get(link)

        search_box = self.find_element('search btn','p',By.NAME)
        search_box.send_keys(f'youtube {VideoId}')
        search_box.submit()
        # breakpoint()
        self.find_element('finding video','a',By.TAG_NAME)
        dicts = self.driver.find_elements(By.TAG_NAME,'a')
        
        for _link in dicts:
            try:
                if f'https://www.youtube.com/watch?v={VideoId}' in _link.get_attribute('href'):
                    
                    self.VideoDuration = self.find_element('Videoduration','ctimestamp',By.CLASS_NAME).text
                    
                    _link.click()
                    return 
            except :...
        
            
    def Video_action(self,comment='',view=False, subscribe_video = False,channel='',like=False):
        self.SkipAds()
        time.sleep(7)        
        if comment : self.CommentOnCurrentVideo(comment)
        if like : self.LikeOnCurrentVideo()
        if subscribe_video: self.click_element('subscribe','//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/yt-button-shape/button')
        if view :self.WatchVideo()
        
    
    def SkipAds(self):
        for i in range(3):
            try: 
                ads = self.find_element('Ads','ytp-ad-player-overlay-flyout-cta',By.CLASS_NAME)
                if ads : 
                    self.click_element('skipads','ytp-ad-skip-button',By.CLASS_NAME)
                    self.click_element('skipads','//*[@id="skip-button:6"]/span/button',timeout=2)
                    self.click_element('skipads','/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button',timeout=1)
                else : break
            except Exception as e:...
    
    def get_videosbyTitle(self,title=''):
        for i in range(5):
            try: 
            
                time.sleep(5)
                if not title : 
                    all_title = self.driver.find_elements(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
                    if all_title: 
                        print(all_title[0].text,'all_title')
                        all_title[0].click()
                        return 
                AllVideoLists = self.driver.find_elements(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/*')
                # breakpoint()
                for i in range(len(AllVideoLists)):
                    VideoText = self.driver.find_element(By.XPATH,f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[{i+1}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
                    if VideoText.text == title:
                        VideoText.click()
                        return
            except Exception as e:...
        
        try: 
            for i in range(1,11):
                video = self.find_element('video',f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
                if video.text == title:
                    video.click()
                    return
        except Exception as e:...
        
            
        all_title = self.driver.find_elements(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
        if all_title: 
            print(all_title[0].text,'all_title')
            all_title[0].click()
        
    def WatchVideo(self):
        
            time.sleep(10)
            self.SkipAds()
            breakpoint()
            currenttimestemp = self.find_element('video time stemp','ytp-time-current',By.CLASS_NAME)
            if currenttimestemp :
                if currenttimestemp.text == '0:00':
                    self.click_element('play button','ytp-play-button',By.CLASS_NAME)
            sec = 0
            # breakpoint()

            if not self.VideoDuration :
                youtube_duration = self.driver.find_elements(By.CLASS_NAME,'ytp-time-duration')
                if youtube_duration:self.VideoDuration = youtube_duration[0].text
                else:self.VideoDuration = self.driver.execute_script(f"return document.getElementsByClassName('ytp-time-duration')[0].textContent")
                
            if self.VideoDuration : 
                youtube_duration = self.VideoDuration.split(':')
                sec += int(youtube_duration[0])*60
                sec += int(youtube_duration[-1])
                random_min_sec = int((sec*70)/100)
                random_max_sec = int((sec*100)/100)
                time_sleeps = int(random.randint(random_min_sec,random_max_sec)/10)
                print(f'Time sleep for {time_sleeps*10} secound')
                for i in range(10):
                    print('Time sleep for :',time_sleeps)
                    time.sleep(time_sleeps)
                    self.SkipAds()
    
    def new_tab(self):
        self.driver.find_element(By.XPATH,'/html/body').send_keys(Keys.CONTROL+'t')

        
    def add_block(self):
        self.driver.get('https://chrome.google.com/webstore/detail/adblock-%E2%80%94-best-ad-blocker/gighmmpiobklfepjocnamgkkbiglidom?gclid=CjwKCAiAhqCdBhB0EiwAH8M_GsHeUlVc0sM7stazecOta-mwkH67ztrQ4e_uT8IdqkcPMgkARUuhjxoCr18QAvD_BwE')
        
        checkExtension = self.find_element('Text of adding btn','/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div')
        if checkExtension:
            if checkExtension.text == "Remove from Chrome" :
                print('there is already added extension in chrome')
                return
        self.click_element('add adblock btn','/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div')
        #switch to alert box
        alert = self.driver.switch_to.active_element
        alert = self.driver.window_handles

        #sleep for a second
        time.sleep(1)
        #accept the alert
        alert.accept()

        time.sleep(1)
        self.user.adblock = True
        self.user.save()
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get('https://www.youtube.com/')
        
    def subscribe_channel(self,link):
        if not link : print('please enter Channel link') ;return False
        self.driver.get(link)
        
        sub_btn = self.find_element('sub btn','//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/tp-yt-paper-button')
        if sub_btn:
            if sub_btn.text == 'Subscribe' :
                sub_btn.click()
                return True
        sub_btn = self.find_element('Subscribe btn','//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/yt-button-shape/button')
        if sub_btn :
            if sub_btn.text == 'Subscribe' :
                sub_btn.click()
                print('Channel subscribed sucess fully'); return True
            else: print('channel is already subscribed'); return True
        else : print("driver couldn't find subscribe btn ") ; return False
        
    def open_video(self,video_link='',subscribe_video=False):
        if not video_link : print('please enter video link');return  False
        self.driver.get(video_link)
        current_video_time = self.find_element('time current of video','//*[@id="movie_player"]/div[33]/div[2]/div[1]/div[1]/span[2]/span[1]',timeout=0).text
        if current_video_time :
            if current_video_time.text == "0:00" :
                self.click_element('large play btn','//*[@id="movie_player"]/div[4]/button')
        return True
        
        if subscribe_video: self.click_element('subscribe','//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/yt-button-shape/button')
            
    def LikeOnCurrentVideo(self):
        
        # self.click_element('Like btn','//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button')
        a = [1,2,3,4,5]
        if random.choice(a) == 1 or 4 :
            self.click_element('Like btn','//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button')
        

    def CommentOnCurrentVideo(self,comment):
            time.sleep(10)
            self.ScrollDown(300)
            comment_input = self.find_element('Comment','//*[@id="placeholder-area"]')    
            entering_comment_actions = ActionChains(self.driver)
            entering_comment_actions.move_to_element(comment_input)
            entering_comment_actions.click()
            for letter in comment:
                entering_comment_actions.send_keys(letter)
                wait_time = random.randint(0,1000)/1000
                entering_comment_actions.pause(wait_time)
            entering_comment_actions.perform()
            
            time.sleep(2)
            sub_btn = self.click_element('submit',"submit-button",By.ID)
            
            if sub_btn : 
                print('comment has been post successfully')
                return True
        
    def getvalue_byscript(self,script = '',reason=''):
        """made for return value from ele or return ele"""
        if reason :print(f'Script execute for : {reason}')
        else:
            print(f'execute_script : {script}')
        value = self.driver.execute_script(f'return {script}')  
        return value
        
    def CloseDriver(self):
        try: 
            
            self.driver.quit()
            print('Driver is closed !')
        except Exception as e: ...
        
            
            
