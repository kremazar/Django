# Generated by Django 2.1.15 on 2020-02-25 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200225_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img',
            name='news',
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.Img'),
        ),
    ]
