from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.name)

class Event(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.name)

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

    def __str__(self):
        return "{} - {}".format(self.name, self.sex, self.age, self.height, self.weight, self.team, self.games, self.event, self.sport, self.medal)
