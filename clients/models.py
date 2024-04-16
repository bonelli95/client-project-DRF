from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    tin = models.CharField(max_length=13, unique=True)
    pin = models.CharField(max_length=9)
    cell = models.CharField(max_length=14)
    active = models.BooleanField()

    def __str__(self):
        return self.name