from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import UrlUsers, Repo


class TestStat(APITestCase):

    def test_status(self):
        lst = ["users", "repo", "stat_repo"]
        for i in lst:
            response = self.client.get(reverse(f"{i}"))
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_data_stat(self):
        url_count = UrlUsers.objects.all().count()
        repo_count = Repo.objects.all().count()
        avg = (url_count / repo_count) if (url_count and repo_count) else 0
        response = self.client.get(reverse('stat'))
        self.assertEqual(response.data['Number of users (projects)'], url_count)
        self.assertIsInstance(response.data['Number of users (projects)'], int)
        self.assertEqual(response.data['Total number of repositories'], repo_count)
        self.assertEqual(response.data['Average number of repositories per user (project)'], avg)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        url_count = UrlUsers.objects.all().count()
        repo_count = Repo.objects.all().count()
        url_create = {"url": "https://github.com/scrapy"}
        self.client.post(reverse('create_url'), url_create)
        response = self.client.get(reverse('create_url'))
        self.assertEqual(UrlUsers.objects.all().count(), url_count + 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        repo_create = {"name_repo": "Muffin", "about": "programm", "site": "Gradane.com", "stars": 4, 
                       "forks": 7, "watching": 17, "commits": 43, "last_commit_author": "Trhe",
                       "last_commit_text": "add", "last_commit_date": "2000", "releases": 0,
                       "last_release_version": "1.2", "last_release_date": "2000", "url_user": url_create['url']
                       }
        self.client.post(reverse('create_repo'), repo_create)
        response = self.client.get(reverse('create_repo'))
        self.assertEqual(Repo.objects.all().count(), repo_count + 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    

