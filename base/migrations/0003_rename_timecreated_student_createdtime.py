# Generated by Django 4.1.7 on 2023-03-10 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_student_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='timeCreated',
            new_name='createdTime',
        ),
    ]
