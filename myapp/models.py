
from django.db import models

class ExampleModel1(models.Model):
    name = models.CharField(max_length=100)

class ExampleModel2(models.Model):
    description = models.TextField()

class ExampleModel3(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    