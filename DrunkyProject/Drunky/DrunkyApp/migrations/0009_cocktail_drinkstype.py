# Generated by Django 2.0.7 on 2018-10-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrunkyApp', '0008_auto_20180911_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='drinksType',
            field=models.ManyToManyField(blank=True, to='DrunkyApp.DrinkType'),
        ),
    ]
