# Generated by Django 3.1 on 2020-12-22 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
