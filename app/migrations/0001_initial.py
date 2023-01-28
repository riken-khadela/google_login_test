# Generated by Django 4.1.4 on 2022-12-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('profile', models.CharField(max_length=255)),
            ],
        ),
    ]