# Generated by Django 5.1 on 2024-09-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0006_remove_staff_details_subject_subject_details_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject_details',
            name='subject_fee',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
