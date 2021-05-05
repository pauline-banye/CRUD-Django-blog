# Generated by Django 3.2 on 2021-05-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paulinsblog', '0009_auto_20210504_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='linken_url',
            new_name='linkedin_url',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]