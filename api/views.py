from django.shortcuts import render
from rest_framework import viewsets
from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer


class BreedDetail(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class DogDetail(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
