# models.py
from django.db import models

class Contact(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.subject
