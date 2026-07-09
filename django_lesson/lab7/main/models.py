from django.db import models
from uuid import uuid4

class Token(models.Model):
    token = models.CharField(max_length=36, unique=True, default=uuid4)
    def __str__(self):
        return self.token

class Good(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name