# Generated by Django 4.1.1 on 2022-10-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0005_alter_profile_displayname_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='displayName',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
    ]
