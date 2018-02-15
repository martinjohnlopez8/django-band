from django.db import models

# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=50, unique=True)
    year_formed = models.IntegerField()
    place_of_origin = models.CharField(max_length=50)
    image_link = models.CharField(max_length=255, default='', blank=True)
    history = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.IntegerField()
    sales = models.IntegerField()
    band = models.ForeignKey('Band', on_delete=models.CASCADE)
    image_link = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=50)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    band = models.ForeignKey('Band', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=50)
    band = models.ForeignKey('Band', on_delete=models.CASCADE)
    instrument = models.CharField(max_length=50)
    image_link = models.CharField(max_length=255, default='', blank=True)
    biography = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name

