"""github_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from users.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", UsersGithubAPIView.as_view(), name="users"),
    path("api/v1/repo/", RepoGithubAPIView.as_view(), name="repo"),
    path("api/v1/stat/", StatGithubAPIView.as_view(), name="stat"),
    path("api/v1/stat-repo/", StatRepoGithubAPIView.as_view(), name="stat_repo"),
    path("api/v2/create-repo/", RepoAPICreate.as_view(), name="create_repo"),
    path("api/v2/create-url/", UrlAPICreate.as_view(), name="create_url"),
]
