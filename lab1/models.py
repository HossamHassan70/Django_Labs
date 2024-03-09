from django.db import models


# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)


class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    track = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
