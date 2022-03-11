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
            lst = Repo.objects.filter(url_user__exact=i['url']).values('name_repo',
                                      'about', 'site', 'stars', 'forks', 'watching', 'commits',
                                      'last_commit_author', 'last_commit_text', 'last_commit_date',
                                      'releases', 'last_release_version', 'last_release_date'
                                      )
            values = [j for j in lst]
            content[i['url']] = values
        return Response(content)


class StatGithubAPIView(APIView):
    def get(self, request):
        count_author = UrlUsers.objects.count()
        count_repo = Repo.objects.count()
        avg_repo = round(count_repo / count_author, 1) if (count_repo and count_author) else 0
        return Response({'Number of users (projects) ': count_author,
                         'Total number of repositories ': count_repo,
                         'Average number of repositories per user (project)': avg_repo
                         })


class StatRepoGithubAPIView(APIView):
    def get(self, request):
        users_lst = UrlUsers.objects.values()
        content = {}
        for i in users_lst:
            lst = Repo.objects.filter(url_user__exact=i['url']).values_list('name_repo', 'commits')
            m = max(lst, key=lambda x: x[1]) if lst else [None, 0]
            avg_stars = Repo.objects.filter(url_user__exact=i['url']).aggregate(avg=Avg('stars'))
            content[i['url']] = {'Repository with the maximum number of commits': m,
                                 'Average number of stars in repositories': avg_stars['avg'] if avg_stars['avg'] is not None else 0
                                }
        return Response(content)


class RepoAPICreate(generics.ListCreateAPIView):
    queryset = Repo.objects.all()
    serializer_class = RepoSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]

   
class UrlAPICreate(generics.ListCreateAPIView):
    queryset = UrlUsers.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]
