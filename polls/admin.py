from django.contrib import admin

# Register your models here.


from polls.models import Poll
admin.site.register(Poll)

from polls.models import MushroomSpot
from leaflet.admin import LeafletGeoAdmin
admin.site.register(MushroomSpot, LeafletGeoAdmin)
