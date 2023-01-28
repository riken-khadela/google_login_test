from django.core.management.base import BaseCommand
from app.models import user
from app.bot import YoutubeBot
import pandas as pd, random

class Command(BaseCommand):
    help = '''to add accounts in database and profile directory
            add accounts in 
            '''
    
    def handle(self, *args, **options):
        
        df = pd.read_csv('1.csv')
        print(len(user.objects.all()))
        # for i in range(len(df)):
        #     email = df.loc[i]['Email']
        #     password = df.loc[i]['Password']
        #     print(email,':',password)
        #     if user.objects.filter(email=email).exists() :
        #         print('Email :',email,'is already exists in database')
        #         continue
        #     profile = 'Profile ' + str(random.randint(100000,9999999))
        #     user_obj = user.objects.get_or_create(
        #         email = str(email).strip(),
        #         password = str(password).strip(),
        #         profile = f'Profile {profile}'
        #         )
        #     print(user_obj)

            # bot = YoutubeBot()
            # bot.get_driver(email,password,profile)
            # bot.add_accounts()
            
        
    