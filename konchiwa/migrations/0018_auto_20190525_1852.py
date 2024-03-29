# Generated by Django 2.2 on 2019-05-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konchiwa', '0017_person_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='registered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
