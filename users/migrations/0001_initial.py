# Generated by Django 4.0.2 on 2022-02-28 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UrlUsers",
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
                ("url", models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Repo",
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
                ("name_repo", models.CharField(max_length=255)),
                ("about", models.TextField(blank=True)),
                ("site", models.CharField(blank=True, max_length=255)),
                ("stars", models.IntegerField()),
                ("forks", models.IntegerField()),
                ("watching", models.IntegerField()),
                ("commits", models.IntegerField()),
                ("last_commit_author", models.TextField()),
                ("last_commit_text", models.TextField()),
                ("last_commit_date", models.CharField(max_length=255)),
                ("releases", models.IntegerField()),
                ("last_release_version", models.CharField(blank=True, max_length=50)),
                ("last_release_date", models.CharField(blank=True, max_length=100)),
                (
                    "url_user",
                    models.ForeignKey(
                        db_column="url_user",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.urlusers",
                        to_field="url",
                    ),
                ),
            ],
        ),
    ]
