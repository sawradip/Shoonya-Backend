# Generated by Django 4.0.4 on 2022-06-16 05:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0023_auto_20220613_1320"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="frozen_users",
            field=models.ManyToManyField(
                blank=True,
                help_text="Frozen Project Users",
                related_name="frozen_project_users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
