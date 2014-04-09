from django.db import models

class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=2)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=2)

##    def __unicode__(self):
##        return unicode(self.month)


class DailyWeather(models.Model):
    month = models.IntegerField()
    day = models.IntegerField()
    temperature = models.DecimalField(max_digits=8, decimal_places=2)
    rainfall = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)

    

    def __unicode__(self):
        return '%s **||** %s' %(self.city, self.state)

##    def __unicode__(self):
##        return unicode(self.state)
##

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

###########################################################################################################################
    from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __unicode__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return '%s' %(self.name)

class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return '%s' %(self.name)

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.FloatField(db_column='rating')
    rating_count = models.IntegerField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, null=True, blank=True, 
                                  on_delete=models.SET_NULL)
    related = models.ManyToManyField('self', db_column='related', blank=True)
    genre = models.ForeignKey(Genre, null=True, blank=True, 
                              on_delete=models.SET_NULL)
    def __unicode__(self):
        return '%s' %(self.title)

class City(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    def __unicode__(self):
        return '%s, %s' %(self.city, self.state)

class BookStore(models.Model):
    name =  models.CharField(max_length=50)
    city = models.ForeignKey('City')
    def __unicode__(self):
        return '%s' %(self.name)
    
class SalesHistory(models.Model):
    bookstore = models.ForeignKey(BookStore)
    book = models.ForeignKey(Book)
    sale_date = models.DateField()
    sale_qty = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __unicode__(self):
        return '%s %s %s' %(self.bookstore, self.book, self.sale_date)
