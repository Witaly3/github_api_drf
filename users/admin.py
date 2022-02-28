from django.contrib import admin

from .models import Repo, UrlUsers

admin.site.register(Repo)
admin.site.register(UrlUsers)
