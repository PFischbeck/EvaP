# Generated by Django 4.2.4 on 2023-09-11 20:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0140_alter_question_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="notes",
            field=models.TextField(blank=True, default="", max_length=1048576, verbose_name="notes"),
        ),
    ]
