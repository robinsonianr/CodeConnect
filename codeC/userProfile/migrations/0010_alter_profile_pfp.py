# Generated by Django 4.1.1 on 2022-11-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0009_alter_profile_pinned_alter_profile_spotlightproj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pfp',
            field=models.ImageField(default='codeC/userProfile/profile_pics/defualt.png', upload_to='profile_pics'),
        ),
    ]
