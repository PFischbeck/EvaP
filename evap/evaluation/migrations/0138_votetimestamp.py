# Generated by Django 4.2.3 on 2023-07-17 20:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0137_use_more_database_constraints"),
    ]

    operations = [
        migrations.CreateModel(
            name="VoteTimestamp",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now, verbose_name="vote timestamp")),
                (
                    "evaluation",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="evaluation.evaluation"),
                ),
            ],
        ),
    ]
