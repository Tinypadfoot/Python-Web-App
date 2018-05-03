# Generated by Django 2.0.2 on 2018-04-28 07:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('natalia_app', '0002_auto_20180428_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 28, 7, 43, 25, 36022, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 28, 7, 43, 25, 34271, tzinfo=utc)),
        ),
    ]