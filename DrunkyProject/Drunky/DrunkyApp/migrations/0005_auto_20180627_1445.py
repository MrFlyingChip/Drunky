# Generated by Django 2.0.6 on 2018-06-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrunkyApp', '0004_sorttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='favourites',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='favourites',
            field=models.IntegerField(default=0),
        ),
    ]
