# Generated by Django 2.2 on 2019-05-31 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('konchiwa', '0025_auto_20190530_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author_ID',
        ),
    ]
