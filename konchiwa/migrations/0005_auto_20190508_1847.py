# Generated by Django 2.2 on 2019-05-08 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konchiwa', '0004_auto_20190508_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
