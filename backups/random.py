from django.core.management.base import BaseCommand
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException,InvalidElementStateException
import time, random, pandas as pd
from app.models import user
from app.bot import YoutubeBot

channel_link = 'https://www.youtube.com/@XANAMetaverse'
video_link = 'https://www.youtube.com/watch?v=2xTqZXoapsc'

class Command(BaseCommand):
    help = '''to add accounts in database and profile directory
            add accounts in 
            '''
    
    def handle(self, *args, **options):
        count = 0
        user_ = user.objects.all().order_by('?')[0]
        try:
            bot = YoutubeBot()
            bot.get_driver(user_.email,user_.password,user_.profile)
            # bot.add_block()
            action = ['Search','DirectLink']
            action = ['Search']
            bot.random_engagement(
                video='https://www.youtube.com/watch?v=5fpBSKmIo2c&ab_channel=XANA',
                title='XANA produced its first avatar fashion show with Hiroko Koshino',
                action='Search',
                view=True,
                subscribe_video=True,
                like=True,
                comment=''
                )
        except :
            bot.CloseDriver()
            
            
        while True:
            try:
                user_ = user.objects.all().order_by('?')[0]
            # for user_ in user.objects.all():
                print(user_.email,user_.password,user_.profile)
                bot = YoutubeBot()
                bot.get_driver(user_.email,user_.password,user_.profile)
                # if not user_.adblock : bot.add_block()
                bot.add_block()
                action = ['Search','DirectLink']
                action = ['Search']
                bot.random_engagement(video='https://www.youtube.com/watch?v=uUvA8hR9kCo',title='XANA produced its first avatar fashion show with Hiroko Koshino',action='Search',view=True,subscribe_video=True,like=True,comment='This is great')
            except :
                bot.CloseDriver()
                print(count)
