# Generated by Django 4.0.4 on 2022-06-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0025_project_src_language_project_tgt_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="src_language",
            field=models.CharField(
                blank=True,
                choices=[
                    ("English", "English"),
                    ("Assamese", "Assamese"),
                    ("Bengali", "Bengali"),
                    ("Bodo", "Bodo"),
                    ("Dogri", "Dogri"),
                    ("Gujarati", "Gujarati"),
                    ("Hindi", "Hindi"),
                    ("Kannada", "Kannada"),
                    ("Kashmiri", "Kashmiri"),
                    ("Konkani", "Konkani"),
                    ("Maithili", "Maithili"),
                    ("Malayalam", "Malayalam"),
                    ("Manipuri", "Manipuri"),
                    ("Marathi", "Marathi"),
                    ("Nepali", "Nepali"),
                    ("Odia", "Odia"),
                    ("Punjabi", "Punjabi"),
                    ("Sanskrit", "Sanskrit"),
                    ("Santali", "Santali"),
                    ("Sindhi", "Sindhi"),
                    ("Sinhala", "Sinhala"),
                    ("Tamil", "Tamil"),
                    ("Telugu", "Telugu"),
                    ("Urdu", "Urdu"),
                ],
                help_text="Source language of the project",
                max_length=50,
                null=True,
                verbose_name="Source Language",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="tgt_language",
            field=models.CharField(
                blank=True,
                choices=[
                    ("English", "English"),
                    ("Assamese", "Assamese"),
                    ("Bengali", "Bengali"),
                    ("Bodo", "Bodo"),
                    ("Dogri", "Dogri"),
                    ("Gujarati", "Gujarati"),
                    ("Hindi", "Hindi"),
                    ("Kannada", "Kannada"),
                    ("Kashmiri", "Kashmiri"),
                    ("Konkani", "Konkani"),
                    ("Maithili", "Maithili"),
                    ("Malayalam", "Malayalam"),
                    ("Manipuri", "Manipuri"),
                    ("Marathi", "Marathi"),
                    ("Nepali", "Nepali"),
                    ("Odia", "Odia"),
                    ("Punjabi", "Punjabi"),
                    ("Sanskrit", "Sanskrit"),
                    ("Santali", "Santali"),
                    ("Sindhi", "Sindhi"),
                    ("Sinhala", "Sinhala"),
                    ("Tamil", "Tamil"),
                    ("Telugu", "Telugu"),
                    ("Urdu", "Urdu"),
                ],
                help_text="Target language of the project",
                max_length=50,
                null=True,
                verbose_name="Target Language",
            ),
        ),
    ]
