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
channel_name = 'XANAMetaverse' 
channel_username = 'XANAMetaverse' 
video_link = 'https://www.youtube.com/watch?v=RhpTougdSz0&ab_channel=XANA' 
VideoTItle = '誰も知らないXANAジェネシスの秘密を初公開！'
VideoId = 'RhpTougdSz0'


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument(
            "--n",
            type=int,
            nargs="?",
            default=1,
        )
        
    def handle(self, *args, **options):
        ThreadNumber = int(options.get('n'))
        random_profile_dic = random.sample(range(1, ThreadNumber+1), ThreadNumber)
        x1 = []
        if ThreadNumber > 10: 
            print('Please run threading system under number of 10')
            return
        for i in random_profile_dic:
            x = threading.Thread(target= self.start_bot, args=(i,))
            x.start()
    
    def start_bot(self,i):
        while True:
            user_ = user.objects.filter(ProfileDict=i).order_by('?')[0]
            user_ = user.objects.filter(ProfileDict=i)[0]
            bot = YoutubeBot()
            try: 
                driver = bot.get_driver(user_.email,user_.password,user_.profile,ChannelName=channel_name,VideoTItle= VideoTItle)
                if driver == False :
                    raise 'Account could not login'
                # bot.add_block()
                # action = ['Search','DirectLink','GoogleSearch','HomeSuggestion','ChannelPage','YahooSearch']
                # # action = ['YahooSearch']
                # action = random.choice(action)
                # video_json = self.video_data()
                # bot.random_engagement(
                #     action=action,
                #     view=True,
                #     subscribe_video=False,
                #     like=True,
                #     comment='',
                #     )
                
            except Exception as e: print(e)
            finally:
                bot.CloseDriver()

    
    def video_data(self):
        video_json = {}
        
        with open("video.txt", "r") as f_in:
            lines = f_in.readlines()
            for line in lines:
                line = line.strip().split(' = ')
                video_json[line[0]] = line[-1]

        return video_json