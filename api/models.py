from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Breed(models.Model):
    SIZES = (
        ('T', 'Tiny'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    name = models.CharField(max_length=32)
    size = models.CharField(max_length=8, choices=SIZES)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class Dog(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=32)
    color = models.CharField(max_length=16)
    favoritefood = models.CharField(max_length=32)
    favoritetoy = models.CharField(max_length=32)
