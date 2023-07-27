from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    views = models.IntegerField(default=0)
    score = models.FloatField(default=0)
    viewed_users = models.ManyToManyField(User, related_name='viewed_movies')
    users_scored = models.ManyToManyField(User, through='MovieScore', related_name='scored_movies')
    
    def __str__(self):
        return self.name

class MovieScore(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    class Meta:
        unique_together = ('movie', 'user')

    def __str__(self):
        return f"{self.movie} - Score: {self.score} - User: {self.user}"


