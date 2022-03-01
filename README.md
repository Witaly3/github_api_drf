# Django REST Framework API for Github scrapping


Cервис по просмотру данных о репозиториях пользователей:

 + API получения ссылок на страницы пользователей (или проектов):  ``` api/v1/users/ ```;
 + API получения репозиториев пользователя (или проекта):  ```api/v2/repo/ ```;
 + API получения общей статистики:  ``` api/v3/stat/```, (1. Количество пользователей (проектов), 2. Общее количество репозиториев, 3. Среднее количество репозиториев у пользователя (проекта) );
 + API получения статистики по одному пользователю (или проекту):  ```api/v4/stat-repo/``` , (1. Репозиторий с максимальным количеством коммитов (название
репозитория - количество), 2. Среднее количество звезд в репозиториях);
+ API по сохранению данных о репозиториях пользователя (или проекта):  ```api/v5/update-repo/<int:pk>/ ```;
+ API по добавлению ссылок на страницы пользователей (или проектов): ``` api/v6/create-url/<int:pk>/ ``` (ссылки валидируются).

Данные сохраняются в базу SQLite 3.

Задействованны 2 модели данных, которые соединены между собой:

```
class UrlUsers(models.Model):
    url = models.URLField(blank=False, unique=True)
  
  
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
    url_user = models.ForeignKey(UrlUsers, to_field='url', db_column='url_user', on_delete=models.CASCADE)

```

## Installation

```
$ git clone git@github.com:Witaly3/github_api_drf.git
$ pip install -r requirements.txt

```

