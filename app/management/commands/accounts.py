from django.core.management.base import BaseCommand
import pandas as pd, random
from app.models import user

class Command(BaseCommand):

    def handle(self, *args, **options):
        df = pd.read_csv('accounts3.csv')
        for i in range(len(df)):
            email = df.loc[i]['email']  
            password = df.loc[i]['password']
            # profile = str(df.loc[i]['profile']).replace('Profile ','').strip()
            profile = str(random.randint(100000,9999999))
            if user.objects.filter(email= str(email).strip()).exists() : 
                print('Account skipped : ', email, profile)
                continue
            user_obj, _ = user.objects.get_or_create(
                email = str(email).strip(),
                password = str(password).strip(),
                profile = f'Profile {profile}'
                )
            print(user_obj.email)