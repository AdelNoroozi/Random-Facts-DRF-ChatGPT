# Generated by Django 4.2 on 2023-04-08 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='email',
        ),
    ]
