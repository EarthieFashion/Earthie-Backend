from django.contrib import admin
from .models import User, OfferSlider, homeBlockOffers, Category, Products, Collection
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','is_staff','date_joined')
    list_filter = ('is_staff','name','email')
    search_fields = ('name','email')

admin.site.register(User,UserAdmin)


class OfferSliderAdmin(admin.ModelAdmin):
    list_display = ('offerName','dateUploaded','published','offerImage')
    list_filter = ('dateUploaded','published')
    search_fields = ('offerName','dateUploaded')

admin.site.register(OfferSlider,OfferSliderAdmin)

class HomeBlockOfferAdmin(admin.ModelAdmin):
    list_display = ('offerName','dateUploaded','offerImage')
    list_filter = ('dateUploaded','published')
    search_fields = ('offerName','dateUploaded')

admin.site.register(homeBlockOffers,HomeBlockOfferAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryName','dateCreated')
    search_fields = ('categoryName','dateCreated')

admin.site.register(Category)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','prodcutName','productPrice','stock','category','is_published')
    list_filter = ('prodcutName','productPrice','category','is_published','stock')
    search_fields = ('prodcutName','category')

admin.site.register(Products,ProductsAdmin)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('collectionName','dateCreated')
    search_fields = ('collectionName','dateCreated')

admin.site.register(Collection,CollectionAdmin)