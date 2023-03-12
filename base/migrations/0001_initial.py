# Generated by Django 4.1.7 on 2023-03-10 10:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('age', models.IntegerField(default=6, validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(99)])),
                ('timeCreated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
