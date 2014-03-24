from django.db import models
from django.utils import timezone
from datetime import datetime

class Poll(models.Model):
    question = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    #pub_date = models.DateTimeField(timezone.now('CET'))
    #pub_date = models.DateTimeField(default=datetime.now,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text
