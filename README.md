# Django REST Framework API for Github scrapping


Service for viewing data about user repositories: 

 + API for getting links to user (or project) pages:  ``` api/v1/users/ ```;
 + API for getting user (or project) repositories:  ```api/v1/repo/ ```;
 +  General statistics API:  ``` api/v1/stat/```, (1. Number of users (projects), 2. Total number of repositories, 3. Average number of repositories per user (project));
 +  API for getting statistics for one user (or project):  ```api/v1/stat-repo/``` , (1. Repository with the maximum number of commits (repository name - number), 2. Average number of stars in repositories);
 + API for saving data about user (or project) repositories:   ```api/v2/create-repo/ ```;
 + API for adding links to user (or project) pages: ``` api/v2/create-url/ ``` .

The data is stored in the Postgresql database.

There are tests on the API for getting general statistics.

Implemented access by API KEY for the API for saving data and links.

2 data models are involved, which are interconnected.

## Installation

```
$ git clone git@github.com:Witaly3/github_api_drf.git
$ pip install -r requirements.txt

```

In ``` settings.py ``` by the address ``` github_api_drf/github_api ``` set your settings for connecting to Postgresql:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'github_db',
        'USER': 'witaly',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
