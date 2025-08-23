from django.contrib.gis.db import models
from location_field.models.spatial import LocationField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return f" {self.id} - {self.title}"

class Business(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = LocationField(geography=True, srid=4326) #pointfiled
    address = models.CharField(max_length=350)
    phone = models.CharField(max_length=11,null=True)
    website = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='Photos/business/%y/%m/%d', null=True, blank=True)
    is_activated = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    business = models.ForeignKey(Business,on_delete=models.CASCADE)
    comment  = models.CharField(max_length=350,null=True,blank=True)
    rate = models.IntegerField()
    created_at = models.DateField(auto_now_add=False)


class Favorite(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    business = models.ForeignKey(Business,on_delete=models.CASCADE)