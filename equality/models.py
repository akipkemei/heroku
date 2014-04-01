from django.db import models

class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=2)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=2)


##
##def enrollment_chart(self):
##    lu = { 'categories' : [ 'Fall 2008', 'Spring 2009','Fall 2009', 'Spring 2010', 'Fall 2010', 'Spring 2011'],\
##             'undergrad' : [18, 22, 30, 34, 40, 47],\
##             'grad' : [1, 2, 4, 4, 5, 7],\
##             'employee' : [2, 3, 0, 1, 1, 2] }
##    lu['total_enrolled'] = [sum(a) for a in zip(lu['undergrad'], lu['grad'],lu['employee'])]
##
##    return render_to_string('admin/course/course/enrollment_chart.html', lu )
##    enrollment_chart.allow_tags = True
