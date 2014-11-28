from django.contrib import *

# Register your models here.


from polls.models import Poll
admin.site.register(Poll)

from polls.models import MushroomSpot
from leaflet.admin import LeafletGeoAdmin
admin.site.register(MushroomSpot, LeafletGeoAdmin)

##from django.contrib.gis import admin as geoadmin
##from polls.models import ApartmentsNY
##
##class ApartmentsNYAdmin(geoadmin.OSMGeoAdmin):
##
##    list_display = ('name', 'city', 'price', 'wifi', 'breakfast')
##    search_fields = ['name']
##    list_filter = ('city',)
##    default_lon =  -8236306.48
##    default_lat =  5028376.23
##    default_zoom = 5
##    
##geoadmin.site.register(ApartmentsNY, ApartmentsNYAdmin)
