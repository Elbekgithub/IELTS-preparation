# Generated by Django 3.0.3 on 2020-04-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_answerlisteningchecked_answerreadingchecked'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerlisteningchecked',
            name='correct',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answerreadingchecked',
            name='correct',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
