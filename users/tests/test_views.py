from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import UrlUsers, Repo


class TestStat(APITestCase):

    def test_status_stat(self):
        response = self.client.get(reverse('stat'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_data_stat(self):
        url_count = UrlUsers.objects.all().count()
        repo_count = Repo.objects.all().count()
        avg = (url_count / repo_count) if (url_count and repo_count) else 0

        response = self.client.get(reverse('stat'))
        self.assertEqual(response.data['Количество пользователей (проектов)'], url_count)
        self.assertIsInstance(response.data['Количество пользователей (проектов)'], int)
        self.assertEqual(response.data['Общее количество репозиториев'], repo_count)
        self.assertEqual(response.data['Среднее количество репозиториев у пользователя (проекта)'], avg)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

