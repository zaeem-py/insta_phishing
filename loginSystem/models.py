from django.db import models

# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)

    def __str__(self) -> str:
          return self.username





