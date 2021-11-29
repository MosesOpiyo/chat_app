from django.contrib.auth.models import User
from django.core.checks import messages
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

from users.models import Account

class Chatbox(models.Model):
    """This defines the behaviours of a project
    Args:
        models ([type]): [description]
    """
    owner = models.ForeignKey(Account,on_delete=models.RESTRICT)
    name = models.CharField(max_length=50,unique=True)
    bio = models.TextField()
    date_created = models.DateField()
    chatbox_pic = models.ImageField()
    
    def __str__(self):
        return self.name
    
    def update(self,new):
        self.name = new.name
        self.bio = new.bio
        self.chatbox_pic = new.chatbox_pic
        self.save()

class Chat(models.Model):
    owner = models.ForeignKey(Account,on_delete=models.RESTRICT)
    chatbox = models.ForeignKey(Chatbox,on_delete=CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.owner.username + self.message + str(self.chatbox.name)


   
    