from rest_framework import serializers
from playbil.models import *


class TheaterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'


class TheatricalDetailSerializer(serializers.ModelSerializer):
    theater = TheaterDetailSerializer()

    class Meta:
        model = Theatrical
        fields = '__all__'


class TheatricalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatrical
        fields = ('id', 'name', 'poster_url')


class WorkerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class TypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class UserClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClient
        fields = '__all__'
