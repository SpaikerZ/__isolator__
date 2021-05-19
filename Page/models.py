from django.db import models
from django.db.models import Model
from django import forms

class Person(models.Model):
    
    name = models.CharField(max_length=20)
    age = models.IntegerField()



    def __str__(self):
        return self.name