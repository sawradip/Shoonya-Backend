# Generated by Django 3.2.14 on 2022-12-06 13:15

from django.db import migrations
from projects.models import Project
from tasks.models import Task, Annotation


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0033_project_published_at"),
    ]

    def populate_published_at_field_for_published_projects(apps, schema_editor):
        projects = Project.objects.filter(published_at__isnull=True).filter(
            is_published=True
        )

        for project in projects:
            tasks = Task.objects.filter(project_id=project)
            task_ids = [task.id for task in tasks]
            annotations = Annotation.objects.filter(task__id__in=task_ids)
            annotations = annotations.order_by("created_at")
            if len(annotations) == 0:
                project.published_at = project.created_at
            else:
                project.published_at = annotations[0].created_at

            project.save()

    operations = [
        migrations.RunPython(populate_published_at_field_for_published_projects)
    ]
