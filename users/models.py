from django.db import models


# Create your models here.
class User(models.Model):
    POSITIONS = [
        ("1", "Developer"),
        ("2", "Designer"),
        ("3", "Manager"),
        ("4", "Administrator")
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    birthdate = models.DateField()
    username = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    position = models.CharField(max_length=255, choices=POSITIONS, blank=True, null=True)

    def __str__(self):
        return self.name
