# Generated by Django 2.1.15 on 2020-02-26 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200225_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='news',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='news.News'),
        ),
    ]
