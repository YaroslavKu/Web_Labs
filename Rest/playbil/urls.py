from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from playbil.views import *

app_name = 'Playbill'
urlpatterns = [
    path('theatrical/create/', TheatricalCreateView.as_view()),
    path('worker/create/', WorkerCreateView.as_view()),
    path('theater/create/', TheatricalCreateView.as_view()),
    path('genre/create/', GenreCreateView.as_view()),
    path('type/create/', TypeCreateView.as_view()),
    path('theater/all/', TheaterListView.as_view()),
    path('theatrical/all/', TheatricalListView.as_view()),
    path('theatrical/<int:pk>/', TheatricalDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt'))
]
