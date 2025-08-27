from django.db.models import Avg
from django.contrib.gis.db import models
from location_field.models.spatial import LocationField
from django.contrib.postgres.indexes import GistIndex

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
    location = LocationField(geography=True,spatial_index=True ,srid=4326) #pointfiled
    address = models.CharField(max_length=350)
    phone = models.CharField(max_length=11,null=True)
    website = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='Photos/business/%y/%m/%d', null=True, blank=True)
    is_activated = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    @property
    def rate_avg(self):
        if self.is_activated:
           
           return getattr(self, "_avg_rate", None) or self.review_set.aggregate(avg=Avg("rate"))["avg"]
    class Meta:
        indexes = [
            GistIndex(fields=["location"]),
        ]
class Review(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    business = models.ForeignKey(Business,on_delete=models.CASCADE)
    comment  = models.CharField(max_length=350,null=True,blank=True)
    rate = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user','business')


class Favorite(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    business = models.ForeignKey(Business,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user','business')