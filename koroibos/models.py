from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=255)

class Event(models.Model):
    name = models.CharField(max_length=255)
    sport = models.ForeignKey('Sport', on_delete=models.PROTECT)


class Olympian(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    team = models.CharField(max_length=255)
    games = models.CharField(max_length=255)
    event = models.ForeignKey('Event', on_delete=models.PROTECT)
    sport = models.ForeignKey('Sport', on_delete=models.PROTECT)
    medal = models.CharField(null=True, max_length=255)

    def total_medals(self):
        if self.medal == None:
            return 0
        else:
            return 1
