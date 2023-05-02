from __future__ import unicode_literals
from django.db import models

class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title

#CLASS BASED VIEW
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class ModelClass(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    price = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "student"


