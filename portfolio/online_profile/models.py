from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name + "-" +  self.email
