# Generated by Django 2.2 on 2019-05-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konchiwa', '0018_auto_20190525_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='registered_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]