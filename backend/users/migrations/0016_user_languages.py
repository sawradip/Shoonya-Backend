# Generated by Django 3.1.14 on 2022-05-09 10:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_user_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('English', 'English'), ('Assamese', 'Assamese'), ('Bengali', 'Bengali'), ('Bodo', 'Bodo'), ('Dogri', 'Dogri'), ('Gujarati', 'Gujarati'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada'), ('Kashmiri', 'Kashmiri'), ('Konkani', 'Konkani'), ('Maithili', 'Maithili'), ('Malayalam', 'Malayalam'), ('Manipuri', 'Manipuri'), ('Marathi', 'Marathi'), ('Nepali', 'Nepali'), ('Odia', 'Odia'), ('Punjabi', 'Punjabi'), ('Sanskrit', 'Sanskrit'), ('Santali', 'Santali'), ('Sindhi', 'Sindhi'), ('Tamil', 'Tamil'), ('Telugu', 'Telugu'), ('Urdu', 'Urdu')], max_length=15, verbose_name='language'), blank=True, default=list, null=True, size=None),
        ),
    ]