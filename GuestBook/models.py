from django.db import models

# Create your models here.
class GuestBook(models.Model):
    name = models.TextField()
    twitter = models.TextField()
    email = models.TextField()
    message = models.TextField()
    spam_me = models.BooleanField()
