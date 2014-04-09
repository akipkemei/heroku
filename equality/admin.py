from django.contrib import admin

# Register your models here.

from django.contrib import admin
from equality.models import MonthlyWeatherByCity
from equality.models import DailyWeather

admin.site.register(MonthlyWeatherByCity)
admin.site.register(DailyWeather)

##
##class CourseAdmin(admin.ModelAdmin):
##    list_display = ( 'course_id', 'title', 'catalog_number', )
##    search_fields = ( 'course_id', 'title', 'catalog_number', )
##    list_filter = ('status',)
##
##    readonly_fields = ('semester_details', 'enrollment_chart' )
##    fieldsets = [
##     ('Course', { 'fields':  [  'course_id', 'title', 'catalog_number', \
##                    'department', 'course_type', 'status', ]}), \
##
##    ('Semester Details', { 'fields':  [  'semester_details',  ]}),\
##    ('Enrollment', { 'fields':  [  'enrollment_chart',  ]}),\
##                    ]
##admin.site.register(Course, CourseAdmin)

