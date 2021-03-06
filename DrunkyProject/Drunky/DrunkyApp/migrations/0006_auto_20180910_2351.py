# Generated by Django 2.0.7 on 2018-09-10 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DrunkyApp', '0005_auto_20180627_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentToAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ManyToManyField(to='DrunkyApp.Account')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='drink',
            name='country',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='DrunkyApp.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commenttoaccount',
            name='comment',
            field=models.ManyToManyField(to='DrunkyApp.Comment'),
        ),
    ]
