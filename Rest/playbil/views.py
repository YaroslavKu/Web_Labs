from django.db.models.functions import Lower
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from playbil.serializers import *
from playbil.models import *


# Create your views here.
class TheatricalCreateView(generics.CreateAPIView):
    serializer_class = TheatricalDetailSerializer


class WorkerCreateView(generics.CreateAPIView):
    serializer_class = WorkerDetailSerializer


class TheaterCreateView(generics.CreateAPIView):
    serializer_class = TheaterDetailSerializer


class TypeCreateView(generics.CreateAPIView):
    serializer_class = TypeDetailSerializer


class GenreCreateView(generics.CreateAPIView):
    serializer_class = GenreDetailSerializer


class TheaterListView(generics.ListAPIView):
    serializer_class = TheaterDetailSerializer
    queryset = Theater.objects.all()


class TheatricalListView(generics.ListAPIView):
    serializer_class = TheatricalListSerializer
    queryset = Theatrical.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'id')


class TheatricalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TheatricalDetailSerializer
    queryset = Theatrical.objects.all()


class UserClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserClient.objects.all()
    serializer_class = UserClientSerializer
