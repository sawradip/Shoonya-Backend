# Generated by Django 3.1.14 on 2022-03-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organizations", "0002_auto_20220214_0533"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invite",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
