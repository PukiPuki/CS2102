from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    phonenumber = models.IntegerField()
    isadmin = models.BooleanField(default=False);
    
class Bid(models.Model):
    biddingstatus = models.CharField(max_length=8)
    biddingprice = models.IntegerField(default=0)
    biddername = models.CharField(max_length=64)
    tid = models.IntegerField(default=0)
    
