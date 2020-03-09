# Generated by Django 3.0.3 on 2020-03-01 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import teacher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MockTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('is_free', models.BooleanField()),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_start', models.DateField(default='')),
                ('speak_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Writing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=teacher.models.upload_location)),
                ('task1', models.TextField()),
                ('task2', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=teacher.models.upload_location)),
                ('mocktest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.MockTest')),
            ],
        ),
        migrations.CreateModel(
            name='Speaking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=teacher.models.upload_location)),
                ('part1', models.TextField()),
                ('part2', models.TextField()),
                ('part3', models.TextField()),
                ('mocktest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.MockTest')),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=teacher.models.upload_location)),
                ('passage1', models.TextField()),
                ('passage2', models.TextField()),
                ('passage3', models.TextField()),
                ('mocktest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.MockTest')),
            ],
        ),
        migrations.CreateModel(
            name='Listening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(upload_to=teacher.models.upload_location)),
                ('pdf', models.FileField(upload_to=teacher.models.upload_location)),
                ('section1', models.TextField()),
                ('section2', models.TextField()),
                ('section3', models.TextField()),
                ('section4', models.TextField()),
                ('mocktest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.MockTest')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1', models.CharField(max_length=100)),
                ('a2', models.CharField(max_length=100)),
                ('a3', models.CharField(max_length=100)),
                ('a4', models.CharField(max_length=100)),
                ('a5', models.CharField(max_length=100)),
                ('a6', models.CharField(max_length=100)),
                ('a7', models.CharField(max_length=100)),
                ('a8', models.CharField(max_length=100)),
                ('a9', models.CharField(max_length=100)),
                ('a10', models.CharField(max_length=100)),
                ('a11', models.CharField(max_length=100)),
                ('a12', models.CharField(max_length=100)),
                ('a13', models.CharField(max_length=100)),
                ('a14', models.CharField(max_length=100)),
                ('a15', models.CharField(max_length=100)),
                ('a16', models.CharField(max_length=100)),
                ('a17', models.CharField(max_length=100)),
                ('a18', models.CharField(max_length=100)),
                ('a19', models.CharField(max_length=100)),
                ('a20', models.CharField(max_length=100)),
                ('a21', models.CharField(max_length=100)),
                ('a22', models.CharField(max_length=100)),
                ('a23', models.CharField(max_length=100)),
                ('a24', models.CharField(max_length=100)),
                ('a25', models.CharField(max_length=100)),
                ('a26', models.CharField(max_length=100)),
                ('a27', models.CharField(max_length=100)),
                ('a28', models.CharField(max_length=100)),
                ('a29', models.CharField(max_length=100)),
                ('a30', models.CharField(max_length=100)),
                ('a31', models.CharField(max_length=100)),
                ('a32', models.CharField(max_length=100)),
                ('a33', models.CharField(max_length=100)),
                ('a34', models.CharField(max_length=100)),
                ('a35', models.CharField(max_length=100)),
                ('a36', models.CharField(max_length=100)),
                ('a37', models.CharField(max_length=100)),
                ('a38', models.CharField(max_length=100)),
                ('a39', models.CharField(max_length=100)),
                ('a40', models.CharField(max_length=100)),
                ('mocktest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.MockTest')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerListening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1', models.CharField(max_length=100)),
                ('a2', models.CharField(max_length=100)),
                ('a3', models.CharField(max_length=100)),
                ('a4', models.CharField(max_length=100)),
                ('a5', models.CharField(max_length=100)),
                ('a6', models.CharField(max_length=100)),
                ('a7', models.CharField(max_length=100)),
                ('a8', models.CharField(max_length=100)),
                ('a9', models.CharField(max_length=100)),
                ('a10', models.CharField(max_length=100)),
                ('a11', models.CharField(max_length=100)),
                ('a12', models.CharField(max_length=100)),
                ('a13', models.CharField(max_length=100)),
                ('a14', models.CharField(max_length=100)),
                ('a15', models.CharField(max_length=100)),
                ('a16', models.CharField(max_length=100)),
                ('a17', models.CharField(max_length=100)),
                ('a18', models.CharField(max_length=100)),
                ('a19', models.CharField(max_length=100)),
                ('a20', models.CharField(max_length=100)),
                ('a21', models.CharField(max_length=100)),
                ('a22', models.CharField(max_length=100)),
                ('a23', models.CharField(max_length=100)),
                ('a24', models.CharField(max_length=100)),
                ('a25', models.CharField(max_length=100)),
                ('a26', models.CharField(max_length=100)),
                ('a27', models.CharField(max_length=100)),
                ('a28', models.CharField(max_length=100)),
                ('a29', models.CharField(max_length=100)),
                ('a30', models.CharField(max_length=100)),
                ('a31', models.CharField(max_length=100)),
                ('a32', models.CharField(max_length=100)),
                ('a33', models.CharField(max_length=100)),
                ('a34', models.CharField(max_length=100)),
                ('a35', models.CharField(max_length=100)),
                ('a36', models.CharField(max_length=100)),
                ('a37', models.CharField(max_length=100)),
                ('a38', models.CharField(max_length=100)),
                ('a39', models.CharField(max_length=100)),
                ('a40', models.CharField(max_length=100)),
                ('mocktest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.MockTest')),
            ],
        ),
    ]