# Generated by Django 2.1.15 on 2020-03-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20200302_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
