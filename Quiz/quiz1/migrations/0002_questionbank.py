# Generated by Django 3.2.8 on 2022-10-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='questionbank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=500)),
                ('opt1', models.CharField(max_length=30)),
                ('opt2', models.CharField(max_length=30)),
                ('opt3', models.CharField(max_length=30)),
                ('opt4', models.CharField(max_length=30)),
                ('corr_opt', models.CharField(max_length=30)),
            ],
        ),
    ]