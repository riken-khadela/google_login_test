from django.core.management.base import BaseCommand
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException,InvalidElementStateException
import time, random, pandas as pd
from app.models import user
from app.bot import YoutubeBot
import threading, random

channel_link = 'https://www.youtube.com/@XANAMetaverse'
video_link = 'https://www.youtube.com/watch?v=2xTqZXoapsc'

class Command(BaseCommand):
    
    
    def handle(self, *args, **options):
        user_ = user.objects.all()
        cnt  = 0
        for user_a in user_:
            cnt+= 1
            user_a.ProfileDict = cnt
            user_a.save()
            if cnt == 10 :
                cnt = 0
        
        
        
        # for user_ in users:
        #     bot = YoutubeBot()
        #     driver = bot.get_driver(user_.email,user_.password,'1',user_.profile)
        #     driver.get('')
        #     bot.CloseDriver()