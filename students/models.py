from django.db import models

# Create your models here.

class StudentsInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
