from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)