from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm
from django import forms
from django.utils.safestring import mark_safe
from django.db.models import Avg, Count
from django.urls import reverse
from datetime import datetime , timedelta
from time import strftime
import math
from django.contrib.auth.models import User
# Create your models here.

class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
        ('None', 'None'),
    )
    parent = TreeForeignKey('self',blank=True,null = True,related_name='children',on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10,choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at= models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True) 

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug': self.slug})

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

class TradeMark(models.Model):
    name = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/') 

    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS = (
        ('True', 'Mở'),
        ('False', 'Khóa'),
    )

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trademark = models.ForeignKey(TradeMark, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/',null=True,default='/images/8ts20a001-so001-m_6A2DGHn.jpg')
    price = models.DecimalField(default = 0,max_digits=100,decimal_places=0)
    reduced_price = models.DecimalField(default= 0,max_digits=100,decimal_places=0, null=True)
    time_end = models.DateField(auto_now_add=False,blank=True,null=True)
    amount = models.IntegerField(default = 0)
    variant = models.CharField(max_length=10, choices = VARIANTS,default = 'None')
    detail = models.TextField()
    detail_long = RichTextUploadingField()
    status = models.CharField(max_length=10,choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at= models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True) 

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image is not None:          
            return mark_safe('<img src = "{}"height = "50" />'.format(self.image.url))
        else:
            return ""

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'slug': self.slug})

    def saving(self):
        if self.reduced_price == 0:
            return 0
        else:
            v = (float(self.price - self.reduced_price)/float(self.price))*100
            return  round(math.ceil(v*100)/100)

    def end(self):
        y = datetime.today().year
        m = datetime.today().month()
        d = datetime.today().day()

        ye = self.end.year
        me = self.end.month()
        de = self.end.day()
        
        a = y - ye
        return int(a)

    def avaregereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt



class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply =  models.ForeignKey('self', null = True, related_name='replies', on_delete =models.SET_NULL)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def children(self):
        return Comment.objects.filter(reply=self)

    @property
    def is_parent(self):
        if self.reply is not None:
            return False
        return True

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'rate']


class Color(models.Model):
    name = models.CharField(max_length= 20)
    code = models.CharField(max_length=10, blank=True, null = True)

    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style ="background-color:{}">Color</p>'.format(self.code))
        else:
            return ""


class Size(models.Model):
    name = models.CharField(max_length= 20)
    code = models.CharField(max_length=10, blank=True, null = True)

    def __str__(self):
        return self.name

class Variants(models.Model):
    title = models.CharField(max_length=100,blank = True, null = True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    color = models.ForeignKey(Color, on_delete= models.CASCADE,blank = True, null = True)
    size = models.ForeignKey(Size, on_delete= models.CASCADE,blank = True, null = True)
    image_id = models.IntegerField(blank = True, null = True,default = 0)
    quantity = models.IntegerField(default = 1)
    price = models.DecimalField(default = 1,max_digits=100,decimal_places=0)

    def __str__(self):
        return self.title

    def image(self):
        img = Images.objects.get(id = self.image_id)
        if img.id is not None:
            varimage = img.image.url
        else:
            varimage = ""
        return varimage

    def image_tag(self):
        img = Images.objects.get(id = self.image_id)
        if img.id is not None:
            return mark_safe('<img src = "{}"height = "50" />'.format(img.image.url))
        else:
            return ""



class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=50,blank=True)
    description = models.TextField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    timeend = models.DateTimeField(auto_now_add=False,blank=True,null=True)
    create_at= models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True) 

    def __str__(self):
        return self.title


