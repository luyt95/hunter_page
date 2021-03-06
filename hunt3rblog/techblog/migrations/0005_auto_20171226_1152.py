# Generated by Django 2.0 on 2017-12-26 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techblog', '0004_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='content',
        ),
        migrations.AddField(
            model_name='log',
            name='action',
            field=models.CharField(choices=[('hit', 'accessed blog'), ('cmt', 'commented post'), ('pos', 'posted')], default='hit', max_length=3),
        ),
        migrations.AddField(
            model_name='log',
            name='ip_addr',
            field=models.CharField(default='unknown', max_length=16),
        ),
        migrations.AddField(
            model_name='log',
            name='message',
            field=models.CharField(default='nothing', max_length=512),
        ),
        migrations.AddField(
            model_name='log',
            name='name',
            field=models.CharField(default='anonymous', max_length=64),
        ),
    ]
