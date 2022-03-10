# Django REST Framework API for Github scrapping


Service for viewing data about user repositories: 

 + API for getting links to user (or project) pages:  ``` api/v1/users/ ```;
 + API for getting user (or project) repositories:  ```api/v2/repo/ ```;
 +  General statistics API:  ``` api/v3/stat/```, (1. Number of users (projects), 2. Total number of repositories, 3. Average number of repositories per user (project));
 +  API for getting statistics for one user (or project):  ```api/v4/stat-repo/``` , (1. Repository with the maximum number of commits (repository name - number), 2. Average number of stars in repositories);
 + API for saving data about user (or project) repositories:   ```api/v5/create-repo/ ```;
 + API for adding links to user (or project) pages: ``` api/v6/create-url/ ``` .

The data is stored in the Postgresql database.

There are tests on the API for getting general statistics.

Implemented access by API KEY for the API for saving data and links.

2 data models are involved, which are interconnected.

## Installation

```
$ git clone git@github.com:Witaly3/github_api_drf.git
$ pip install -r requirements.txt

```

