from django.db import models


class Workout(models.Model):
    activity = models.CharField(max_length=200)
    duration = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.activity