from django.db import models


class contestant(models.Model):
    uid = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    score = models.IntegerField(max_length=3, null=True)



class questionbank(models.Model):
    questions = models.CharField(max_length=500)
    opt1 = models.CharField(max_length=30)
    opt2 = models.CharField(max_length=30)
    opt3 = models.CharField(max_length=30)
    opt4 = models.CharField(max_length=30)
    corr_opt = models.CharField(max_length=30)
