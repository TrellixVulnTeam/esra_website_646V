from django.db import models


class ContactInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

