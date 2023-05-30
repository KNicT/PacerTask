from django.db import models

# Create your models here.
class Scores(models.Model):
    userId = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"User ID: {self.userId}, Score: {self.score}"
    
