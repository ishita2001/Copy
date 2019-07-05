from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE , primary_key = True)
    name = models.CharField(max_length = 50)
    #password = models.CharField(max_length = 15)
    contact_no = models.CharField(max_length = 12, blank = True)   #To be changed to false
    email_id = models.CharField(max_length = 20, blank = True)
    website = models.CharField(max_length = 50, blank = True)
    #rating = 


class Product(models.Model):
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 25)
    price = models.IntegerField(blank=True)
    seller = models.ForeignKey(User, on_delete = models.CASCADE)
    #flag to differentiate crawled data from signed up data
    crawled = models.BooleanField(default=False)    
    rating = models.FloatField(default=0)
    quantity = models.CharField(max_length = 50)
    #feedback = models.OneToOneField(Feedback)
    
    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key = True)
    name = models.CharField(max_length = 50)
    #password = models.CharField(max_length = 15)
    contact_no = models.CharField(max_length = 12, blank = True)   #To be changed to false
    email_id = models.CharField(max_length = 20, blank = True)
    product = models.ManyToManyField(Product)
    #feedback
    #wishlist


