# Generated by Django 3.2.8 on 2022-10-14 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz1', '0005_contestant_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='score',
            field=models.IntegerField(blank=True, max_length=3),
        ),
    ]
