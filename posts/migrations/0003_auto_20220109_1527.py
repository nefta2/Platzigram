# Generated by Django 3.2.9 on 2022-01-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]