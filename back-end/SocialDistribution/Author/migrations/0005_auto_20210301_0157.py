# Generated by Django 3.1.7 on 2021-03-01 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0004_comment_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='recipient_id',
            new_name='liker_id',
        ),
        migrations.AddField(
            model_name='like',
            name='comment_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Author.comment'),
        ),
        migrations.AddField(
            model_name='like',
            name='post_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Author.post'),
        ),
    ]
