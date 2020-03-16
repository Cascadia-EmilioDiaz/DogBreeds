from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import BreedDetail, DogDetail

router = routers.DefaultRouter()
router.register('breeds', BreedDetail)
router.register('dogs', DogDetail)

urlpatterns = [
    path('', include(router.urls)),
]
