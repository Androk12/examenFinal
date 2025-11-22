from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import project
from .serializers import ProjectSerializer


class ProjectPag(PageNumberPagination):
    tamaño = 10


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serialize = ProjectSerializer
    pagina = ProjectPag

    def traeQueryset(self):
        queryset = project.objects.all()
        autor = self.request.query_params.get('author')
        if autor:
            queryset = queryset.filter(autor = autor)
        return queryset
