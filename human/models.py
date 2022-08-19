from django.db import models

# Create your models here.
class Human(models.Model):
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.DateField()
    inn = models.CharField(max_length=14)

    def __str__(self):
        return self.firstname
