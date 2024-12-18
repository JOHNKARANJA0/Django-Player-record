from django.db import models

class PLAYER(models.Model):
    pid = models.CharField(max_length=10)
    pname = models.CharField(max_length=50)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    game = models.CharField(max_length=30)
    region = models.CharField(max_length=35)
    class Meta:
        db_table = 'player'