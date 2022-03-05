from django.db.models import Avg
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated


from .models import Repo, UrlUsers
from .serializer import RepoSerializer, UrlSerializer


class UsersGithubAPIView(APIView):
    def get(self, request):
        url_all = UrlUsers.objects.values('url')
        return Response({'url': [i['url'] for i in url_all]})


class RepoGithubAPIView(APIView):
    def get(self, request):
        users_lst = UrlUsers.objects.values()
        content = {}
        for i in users_lst:
            lst = Repo.objects.filter(url_user__exact=i['url']).values('name_repo')
            values = [j['name_repo'] for j in lst]
            content[i['url']] = values
        return Response(content)


class StatGithubAPIView(APIView):
    def get(self, request):
        count_author = UrlUsers.objects.count()
        count_repo = Repo.objects.count()
        avg_repo = round(count_repo / count_author, 1) if (count_repo and count_author) else 0
        return Response({'Количество пользователей (проектов)': count_author,
                         'Общее количество репозиториев': count_repo,
                         'Среднее количество репозиториев у пользователя (проекта)': avg_repo
                         })


class StatRepoGithubAPIView(APIView):
    def get(self, request):
        users_lst = UrlUsers.objects.values()
        content = {}
        for i in users_lst:
            lst = Repo.objects.filter(url_user__exact=i['url']).values_list('name_repo', 'commits')
            m = max(lst, key=lambda x: x[1])
            avg_stars = Repo.objects.filter(url_user__exact=i['url']).aggregate(avg=Avg('stars'))
            content[i['url']] = {m[0]: m[1]}, avg_stars
        return Response(content)


class RepoAPICreate(generics.ListCreateAPIView):
    queryset = Repo.objects.all()
    serializer_class = RepoSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]

   
class UrlAPICreate(generics.ListCreateAPIView):
    queryset = UrlUsers.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]

