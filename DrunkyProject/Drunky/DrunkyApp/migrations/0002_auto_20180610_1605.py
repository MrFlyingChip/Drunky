# Generated by Django 2.0.5 on 2018-06-10 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DrunkyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DrunkyApp.Product')),
            ],
            bases=('DrunkyApp.product',),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='votes',
            new_name='likes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='averageMark',
        ),
        migrations.AddField(
            model_name='cocktailtype',
            name='description',
            field=models.CharField(default='null', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='description',
            field=models.CharField(default='null', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drinktype',
            name='description',
            field=models.CharField(default='null', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cocktail',
            name='cocktailType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DrunkyApp.CocktailType'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='drinks',
            field=models.ManyToManyField(to='DrunkyApp.Drink'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='ingredients',
            field=models.ManyToManyField(to='DrunkyApp.Ingredient'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='tools',
            field=models.ManyToManyField(to='DrunkyApp.Tool'),
        ),
    ]
