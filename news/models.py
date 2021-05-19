from django.db import models
from django.db.models import Model
from django import forms

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length = 120)
    post = models.TextField()
    date = models.DateTimeField(
        verbose_name=("Creation date"), 
    )

    def __str__(self):
        return self.title