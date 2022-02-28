from rest_framework import serializers
from .models import *


class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = "__all__"


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlUsers
        fields = "__all__"
