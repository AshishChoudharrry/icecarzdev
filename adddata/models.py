from django.db import models
from autoslug import AutoSlugField
class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="brand/",max_length=500, default=None, null=True)
    slug = AutoSlugField(populate_from='name', unique = True, null=True, default = None)
    def __str__(self):
        return self.name
    
class Car (models.Model): 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    carimage = models.ImageField(upload_to="cars/",max_length=500, default=None, null=True )
    slug = AutoSlugField(populate_from='name', unique = True, null=True, default = None)
    def __str__(self):
        return self.name
    
    
class CarInfo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    engine = models.CharField(max_length=50)
    transmission = models.CharField( max_length=50)
    power = models.IntegerField()
    torque = models.IntegerField()
    to100 = models.FloatField()
    year = models.IntegerField()
    summry = models.TextField()
    infoimage = models.ImageField(upload_to="car/",max_length=500, default=None, null=True )
    def __str__(self):
        return self.car.name
 
class PopularBrands(models.Model):
    popular = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    def __str__(self):
        return self.popular.name  
    
class PopularCars(models.Model):
    popular = models.ForeignKey( Car, on_delete=models.CASCADE)
    def __str__(self):
        return self.popular.name

