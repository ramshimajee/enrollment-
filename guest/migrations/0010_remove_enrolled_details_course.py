# Generated by Django 5.1 on 2024-09-10 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0009_remove_enrolled_details_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolled_details',
            name='course',
        ),
    ]
