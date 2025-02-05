# Generated by Django 3.1 on 2020-12-28 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acquired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owned', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Yes', max_length=1)),
                ('date', models.DateField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.coin')),
            ],
        ),
    ]
