from django.db import models


class User(models.Model):
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    # related Player?

class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birthday = models.DateField()
    gender = models.CharField(max_length=1,
                                choices=GENDER_CHOICES,
                                default=OTHER)


class Game(models.Model):
    location = models.CharField(max_length=30)
    datePlayed = models.DateField()
    dateAdded = models.DateTimeField(auto_now_add=True)
    #addedBy = models.ForeignKey(User, on_delete=models.PROTECT)


class Score(models.Model):
    # this model will be used to hold scores:
    # scores are unique with respect to player and Games
    # this should be all thats needed to build games from


    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    score1 = models.IntegerField(verbose_name='Round 1 Score')
    score2 = models.IntegerField(verbose_name='Round 2 Score')
    score3 = models.IntegerField(verbose_name='Round 3 Score')
    score4 = models.IntegerField(verbose_name='Round 4 Score')
    score5 = models.IntegerField(verbose_name='Round 5 Score')
    score6 = models.IntegerField(verbose_name='Round 6 Score')
    score7 = models.IntegerField(verbose_name='Round 7 Score')
