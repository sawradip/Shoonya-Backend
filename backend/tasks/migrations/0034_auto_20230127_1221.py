# Generated by Django 3.2.16 on 2023-01-27 12:21


from django.db import migrations, models
from django.db.models import Q
from tasks.models import Annotation , Task
from tqdm import tqdm


def change_existing_task_annotation_status_in_db(apps, schema_editor):
    tasks = apps.get_model("tasks", "Task")
    annotations = apps.get_model("tasks", "Annotation")
    db_alias = schema_editor.connection.alias
    taskobj = tasks.objects.using(db_alias).all()
    annotator_annotobj = annotations.objects.using(db_alias).filter(
        parent_annotation_id=None
    )
    reviewer_annotobj = annotations.objects.using(db_alias).filter(
        parent_annotation_id__isnull=False
    )

    # #create empty annotations for  unlabeled and skipped  pulled tasks .

    pulled_unlabeled_skipped_tasks = Task.objects.filter(
        task_status__in=["unlabeled", "skipped"], annotation_users__isnull=False
    )

    pulled_tasks_list = []
    for tas in tqdm(pulled_unlabeled_skipped_tasks):
        for user1 in tas.annotation_users.all():
            base_annotation_obj = Annotation(
                result=[],
                task=tas,
                completed_by=user1,
            )
            pulled_tasks_list.append(base_annotation_obj)

    Annotation.objects.bulk_create(pulled_tasks_list, 512)

    # annotator annotation objects status update
    annot1 = annotator_annotobj.filter(task__task_status__in=["unlabeled", "freezed"])
    ann1_list = []
    for ann1 in tqdm(annot1):
        setattr(ann1, "annotation_status", "unlabeled")
        ann1_list.append(ann1)
    Annotation.objects.bulk_update(ann1_list, ["annotation_status"], 512)

    annot2 = annotator_annotobj.filter(
        task__task_status__in=[
            "labeled",
            "accepted",
            "accepted_with_changes",
            "to_be_revised",
        ]
    )
    annot2_list = []
    for ann2 in tqdm(annot2):
        setattr(ann2, "annotation_status", "labeled")
        annot2_list.append(ann2)
    Annotation.objects.bulk_update(annot2_list, ["annotation_status"], 512)

    annot3 = annotator_annotobj.filter(task__task_status="skipped")
    annot3_list = []
    for ann3 in tqdm(annot3):
        setattr(ann3, "annotation_status", "skipped")
        annot3_list.append(ann3)
    Annotation.objects.bulk_update(annot3_list, ["annotation_status"], 512)

    annot4 = annotator_annotobj.filter(task__task_status="draft")
    annot4_list = []
    for ann4 in tqdm(annot4):
        setattr(ann4, "annotation_status", "draft")
        annot4_list.append(ann4)
    Annotation.objects.bulk_update(annot4_list, ["annotation_status"], 512)

    # reviewer annotation objects status update
    annot5 = reviewer_annotobj.filter(
        task__task_status__in=["labeled", "unlabeled", "freezed"]
    )
    annot5_list = []
    for ann5 in tqdm(annot5):
        setattr(ann5, "annotation_status", "unreviewed")
        annot5_list.append(ann5)
    Annotation.objects.bulk_update(annot5_list, ["annotation_status"], 512)

    annot6 = reviewer_annotobj.filter(task__task_status="accepted")
    annot6_list = []
    for ann6 in tqdm(annot6):
        setattr(ann6, "annotation_status", "accepted")
        annot6_list.append(ann6)
    Annotation.objects.bulk_update(annot6_list, ["annotation_status"], 512)

    annot7 = reviewer_annotobj.filter(task__task_status="skipped")
    annot7_list = []
    for ann7 in tqdm(annot7):
        setattr(ann7, "annotation_status", "skipped")
        annot7_list.append(ann7)
    Annotation.objects.bulk_update(annot7_list, ["annotation_status"], 512)

    annot8 = reviewer_annotobj.filter(task__task_status="draft")
    annot8_list = []
    for ann8 in tqdm(annot8):
        setattr(ann8, "annotation_status", "draft")
        annot8_list.append(ann8)
    Annotation.objects.bulk_update(annot8_list, ["annotation_status"], 512)

    annot9 = reviewer_annotobj.filter(task__task_status="to_be_revised")
    annot9_list = []
    for ann9 in tqdm(annot9):
        setattr(ann9, "annotation_status", "to_be_revised")
        annot9_list.append(ann9)
        parent = ann9.parent_annotation
        setattr(parent, "annotation_status", "to_be_revised")
        annot9_list.append(parent)
    Annotation.objects.bulk_update(annot9_list, ["annotation_status"], 512)

    annot10 = reviewer_annotobj.filter(task__task_status="accepted_with_changes")
    annot10_list = []
    for ann10 in tqdm(annot10):
        setattr(ann10, "annotation_status", "accepted_with_minor_changes")
        annot10_list.append(ann10)
    Annotation.objects.bulk_update(annot10_list, ["annotation_status"], 512)


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0033_delete_tasklock"),
    ]

    operations = [
        migrations.AddField(
            model_name="annotation",
            name="annotation_status",
            field=models.CharField(
                choices=[
                    ("unlabeled", "unlabeled"),
                    ("labeled", "labeled"),
                    ("skipped", "skipped"),
                    ("draft", "draft"),
                    ("unreviewed", "unreviewed"),
                    ("accepted", "accepted"),
                    ("accepted_with_minor_changes", "accepted_with_minor_changes"),
                    ("accepted_with_major_changes", "accepted_with_major_changes"),
                    ("to_be_revised", "to_be_revised"),
                ],
                default="unlabeled",
                max_length=100,
                verbose_name="annotation_status",
            ),
        ),
        migrations.RunPython(change_existing_task_annotation_status_in_db),
    ]
