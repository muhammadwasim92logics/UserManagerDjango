from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255, default="Unknown")  # Set a default value
    email = models.CharField(max_length=300, default="Unknown")

    # id = models.TextField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
