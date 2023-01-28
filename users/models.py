from django.db import models


class UrlUsers(models.Model):
    url = models.URLField(blank=False, unique=True)

    def __str__(self):
        return self.url


class Repo(models.Model):
    name_repo = models.CharField(max_length=255, blank=False)
    about = models.TextField(blank=True)
    site = models.CharField(max_length=255, blank=True)
    stars = models.IntegerField(blank=False)
    forks = models.IntegerField(blank=False)
    watching = models.IntegerField(blank=False)
    commits = models.IntegerField(blank=False)
    last_commit_author = models.TextField(blank=False)
    last_commit_text = models.TextField(blank=False)
    last_commit_date = models.CharField(max_length=255, blank=False)
    releases = models.IntegerField(blank=False)
    last_release_version = models.CharField(max_length=50, blank=True)
    last_release_date = models.CharField(max_length=100, blank=True)
    url_user = models.ForeignKey(
        UrlUsers, to_field="url", db_column="url_user", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name_repo
