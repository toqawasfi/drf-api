# Generated by Django 4.2.3 on 2023-07-18 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_rename_owner_post_user_comment_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='auther',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='auther',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='social.post'),
        ),
    ]