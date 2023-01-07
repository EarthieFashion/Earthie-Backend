from django.db import models

# custom user model based on email
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


# offers model

class OfferSlider(models.Model):
    offerName = models.CharField(max_length=255)
    offerImage = models.ImageField(upload_to='images/Offers/')
    dateUploaded = models.TimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.offerName


class homeBlockOffers(models.Model):
    offerName = models.CharField(max_length=255)
    offerImage = models.ImageField(upload_to='images/Offers/')
    dateUploaded = models.TimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    linkToOffer = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.offerName

class Category(models.Model):
    categoryName = models.CharField(max_length=255)
    dateCreated = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.categoryName
        
class Collection(models.Model):
    collectionName = models.CharField(max_length=255)
    dateCreated = models.TimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    collectionImage = models.ImageField(upload_to='images/collection/', null=True)

    def __str__(self):
        return self.collectionName

class Products(models.Model):
    productSKU = models.CharField(max_length=255)
    prodcutName = models.CharField(max_length=255)
    productPrice = models.CharField(max_length=255)
    stock = models.CharField(max_length=255)
    productImage = models.ImageField(upload_to='images/products/')
    miscImage1 = models.ImageField(upload_to='images/products/', null=True, blank=True, default="")
    miscImage2 = models.ImageField(upload_to='images/products/', null=True, blank=True, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True, default="")
    is_published = models.BooleanField(default=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    dateAdded = models.DateTimeField(auto_now_add=True, null=True)
    material = models.CharField(max_length=255, default='100% Cotton')
    care = models.CharField(max_length=255, default='Machine Wash')

    def __str__(self):
        return self.prodcutName


class Offers(models.Model):
    offerName =  models.CharField(max_length=255)
    offerProduct = models.ForeignKey(Products, on_delete=models.CASCADE)
    offerPrice = models.CharField(max_length=255)
    offerBy = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.offerName
