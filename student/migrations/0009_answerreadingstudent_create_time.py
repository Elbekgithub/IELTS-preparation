# Generated by Django 3.0.3 on 2020-03-13 05:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_answerlisteningstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerreadingstudent',
            name='create_time',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2020, 3, 13, 5, 51, 10, 249585, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
