from django.db import models


# Create your models here.

class Users(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=40)


class Artists(models.Model):
    artistName = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.artistName


class Album(models.Model):
    albumName = models.CharField(max_length=100)
    albumArtist = models.ForeignKey('Artists', models.DO_NOTHING)
    noSongs = models.IntegerField()
