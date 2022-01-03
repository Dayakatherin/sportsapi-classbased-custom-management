from django.db import models

# Create your models here.
class sports(models.Model):
    name = models.CharField(max_length=30)
    sport = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name