# Generated by Django 3.1.7 on 2021-03-01 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='commentCount',
            field=models.IntegerField(default=0),
        ),
    ]