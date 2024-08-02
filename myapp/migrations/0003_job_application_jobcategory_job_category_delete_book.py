# Generated by Django 5.0.7 on 2024-08-02 12:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_book_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("requirements", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("published_date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Application",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("resume", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Submitted", "Submitted"),
                            ("Reviewed", "Reviewed"),
                            ("Interviewed", "Interviewed"),
                            ("Hired", "Hired"),
                            ("Rejected", "Rejected"),
                        ],
                        default="Submitted",
                        max_length=20,
                    ),
                ),
                ("published_date", models.DateField(auto_now_add=True)),
                (
                    "job_posting",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.job",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobCategory",
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
                ("name", models.CharField(max_length=100)),
                ("published_date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="job",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.jobcategory",
            ),
        ),
        migrations.DeleteModel(
            name="Book",
        ),
    ]