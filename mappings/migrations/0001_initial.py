# Generated by Django 5.1.7 on 2025-03-13 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("doctors", "0001_initial"),
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientDoctorMapping",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("assigned_date", models.DateTimeField(auto_now_add=True)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doctors.doctor"
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients.patient",
                    ),
                ),
            ],
            options={
                "unique_together": {("patient", "doctor")},
            },
        ),
    ]
