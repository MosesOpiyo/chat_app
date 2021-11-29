from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Chatbox(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    members = models.OneTo

class Message(models.Model):
    text = models.TextField()
    texter = models.ForeignKey(User,on_delete=CASCADE)
    time_input = models.TimeField()

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(blank=True,null=True,)
