# Generated by Django 2.2 on 2019-05-27 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('konchiwa', '0021_auto_20190527_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='C_title',
            new_name='title',
        ),
    ]
