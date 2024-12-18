from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    birthdate = models.DateField()
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.name
