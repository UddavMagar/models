from django.db import models


class Bungalow(models.Model):
    houseimg = models.ImageField(upload_to='house/')
    price = models.BigIntegerField(default=0)
    address = models.TextField(max_length=100)
    area = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    bathroom = models.IntegerField(default=0)
    parking = models.IntegerField(default=0)
    owner = models.TextField(max_length=200)
    view = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    
class Aboutproperty(models.Model):
    bungalow = models.ForeignKey(Bungalow, on_delete=models.CASCADE)
    property_detail = models.TextField(max_length=2000)

class Societyamenities(models.Model):
    bungalow = models.ForeignKey(Bungalow, on_delete=models.CASCADE)
    amenitie = models.CharField(max_length=100)


class Gallery(models.Model):
    bungalow = models.ForeignKey(Bungalow, on_delete=models.CASCADE)
    houseimages1 = models.ImageField(upload_to='gallery/')
    houseimages2 = models.ImageField(upload_to='gallery/')
    houseimages3 = models.ImageField(upload_to='gallery/')


class Location(models.Model):
    bungalow = models.ForeignKey(Bungalow, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)



class Fieldvisit(models.Model):
    bungalow = models.ForeignKey(Bungalow, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(default=0)

    
