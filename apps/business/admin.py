from django.contrib import admin
from django.utils.html import format_html

from apps.business.models import Business, Category, Favorite, Review

from unfold.admin import ModelAdmin


# Register your models here.
@admin.register(Business)
class BusinessAdmin(ModelAdmin):
    fields = ['name','description','owner','category','address',"location",'phone','website','image',"is_activated"]
    list_display = ['name', 'owner', 'category', 'created_at',"is_activated"]
    list_editable = ['is_activated']

   
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    fields = ['title']
    list_display = ['id','title']
   
@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    fields = ['user','business','comment','rate']
    list_display = ['id','user','business','comment','rate',"created_at"]
   
@admin.register(Favorite)
class FavoriteAdmin(ModelAdmin):
    fields = ['user','business']
    list_display = ['id','user','business']