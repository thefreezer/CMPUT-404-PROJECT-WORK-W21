# Generated by Django 3.1.7 on 2021-02-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0002_auto_20210222_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='github',
            field=models.TextField(null=True),
        ),
    ]
