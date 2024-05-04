from django.db import models


# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.title