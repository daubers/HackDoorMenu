from django.db import models


# Create your models here.
class GuestBook(models.Model):
    name = models.TextField()
    email = models.EmailField()
    date = models.DateTimeField()
    comment = models.TextField()
    anonymous = models.BooleanField()