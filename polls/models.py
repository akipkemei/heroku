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
##########################################################################
class User (models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):              
        return self.name

class Message (models.Model):
    content = models.TextField(max_length=140, null=True, blank=True)
    user = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    longitude = models.FloatField(max_length=255,default=0)
    latitude = models.FloatField(max_length=255,default=0)
    accuracy = models.FloatField(max_length=255,default=0)

    def __unicode__(self):              
        return self.content

##########################################################################

from djgeojson.fields import PointField
from django.db import models

class MushroomSpot(models.Model):

    geom = PointField()
################################################################################
###########################################################################################################################
###########################################################################################################################
from django.contrib.gis.db import models
from django.contrib.gis import admin
from django.utils import timezone
from autoslug import AutoSlugField
from easy_thumbnails.fields import ThumbnailerImageField

def image_upload_folder(instance, filename):
    return "apartments_images/%s" % (filename)

choices_city = (        
    ('New York City', 'NYC'),
    ('Syracuse', 'Syracuse'),
    ('Buffalo', 'Buffalo'),
    ('Rochester', 'Rochester'),
    ('Yonkers', 'Yonkers')
)

class ApartmentsNY(models.Model):
    name = models.CharField("Name of the apartment", max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True) 
    city = models.CharField("City", max_length=70, choices=choices_city)
    price = models.IntegerField("Price per night [$]")
    wifi = models.BooleanField("WiFi", default=False)
    breakfast = models.BooleanField("Breakfast", default=False)
    image = ThumbnailerImageField(upload_to=image_upload_folder, blank=True)

    geom = models.PointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Apartments in NY"

admin.site.register(ApartmentsNY, admin.OSMGeoAdmin)
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################

#from django.contrib.gis.db import models as geomodels
##from django.contrib.gis.db import models
##
##class Pointa(models.Model):
##    name = models.CharField(max_length=50)
##    coords = models.PointField()
##    objects = models.GeoManager()
    
class Lalal (models.Model):
    content = models.TextField(max_length=140, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)
