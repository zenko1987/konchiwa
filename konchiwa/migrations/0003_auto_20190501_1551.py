# Generated by Django 2.2 on 2019-05-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konchiwa', '0002_auto_20190501_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='journal_ID',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='journal',
            name='journal_ID',
            field=models.CharField(max_length=128),
        ),
    ]