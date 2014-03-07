from django.db import models
from datetime import datetime
#from django.utils import timezone
#from pytz import UTC


# Create your models here.
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    #pub_date = models.DateTimeField(default=datetime.now,blank=True)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
