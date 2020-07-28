from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from product.models import Product

# Create your models here.

    

class UserProfile(models.Model):
    SEX_CHOICES = (
        ('Nữ', 'Nữ',),
        ('Nam', 'Nam',),
        ('Chưa xác định', 'Chưa xác định',),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=20,
        choices=SEX_CHOICES,
        null= True,
        default="Chưa xác định",
    )
    phone = models.CharField(max_length=12, blank=True)
    name = models.CharField(blank=True, max_length=30)
    address = models.CharField(blank=True, max_length=150)   
    district = models.CharField(blank=True, max_length=150) 
    city = models.CharField(max_length=50, blank=True)
    
    name1 = models.CharField(null = True,blank=True, max_length=30)
    address1 = models.CharField(null = True, blank=True, max_length=150)
    district1 = models.CharField(null = True,blank=True, max_length=150)
    city1 = models.CharField(null = True,max_length=50, blank=True)
    image = models.ImageField(blank=True,upload_to='images/user/')
    
    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src = "{}"height = "50" />'.format(self.image.url))

    image_tag.short_description = 'Image'

class City(models.Model):
    name = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name

class District(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name

class Ward(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name













