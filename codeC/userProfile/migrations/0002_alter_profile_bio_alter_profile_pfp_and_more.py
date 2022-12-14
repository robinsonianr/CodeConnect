# Generated by Django 4.1.1 on 2022-10-07 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pfp',
            field=models.ImageField(default='profile_pics/default.png', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
