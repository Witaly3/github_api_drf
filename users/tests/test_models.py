from rest_framework.test import APITestCase
from ..models import UrlUsers, Repo


class TestModel(APITestCase):
    def test_creates_url(self):
        url = UrlUsers.objects.create(url="https://github.com/scrapy")
        self.assertEqual(url, url)
        repo = Repo.objects.create(
            name_repo="Muffin",
            about="yes",
            site="Gradane",
            stars=4,
            forks=7,
            watching=17,
            commits=43,
            last_commit_author="Trhe",
            last_commit_text="add",
            last_commit_date="43",
            releases=0,
            last_release_version="1.2",
            last_release_date="2000",
            url_user=url,
        )
        self.assertEqual(repo, repo)
