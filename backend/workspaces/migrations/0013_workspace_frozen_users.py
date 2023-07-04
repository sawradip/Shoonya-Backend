# Generated by Django 3.2.14 on 2023-05-01 14:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("workspaces", "0012_alter_workspace_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="workspace",
            name="frozen_users",
            field=models.ManyToManyField(
                blank=True,
                help_text="Frozen Workspace Users",
                related_name="frozen_workspace_users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
