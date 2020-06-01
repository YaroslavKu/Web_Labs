from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Type(models.Model):
    name = models.CharField(max_length=45)


class Genre(models.Model):
    name = models.CharField(max_length=45)


class Theater(models.Model):
    name = models.CharField(max_length=255)
    photo_url = models.URLField(default='https://google.com')
    address = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    schedule = models.CharField(max_length=255, default='')
    description = models.TextField(max_length=1023, default='')


class Worker(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    role = models.CharField(max_length=45)


class Theatrical(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=1023)
    time = models.DateTimeField()
    duration = models.IntegerField()
    tickets_url = models.URLField()
    poster_url = models.URLField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    worker = models.ManyToManyField(Worker)


class UserClient(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
