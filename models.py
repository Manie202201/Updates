from django.db import models
from importlib.resources import contents
from pyexpat import model
from turtle import title


class Artiste (models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()


class Song (models.Model):
    title = models.CharField(max_length=400)
    date_released = models.IntegerField()
    likes = models.IntegerField()
    Artiste_id = models.ForeignKey( on_delete=models.PROTECT)
    
class Lyric(models.Model):
    contents = models.TextField(max_length=1000)
    song_id = models.ForeignKey("app.Model", verbose_name=(), on_delete=models.PROTECT
    )

    
