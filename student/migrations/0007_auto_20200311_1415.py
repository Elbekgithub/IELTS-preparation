# Generated by Django 3.0.3 on 2020-03-11 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0006_auto_20200311_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerreadingstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
