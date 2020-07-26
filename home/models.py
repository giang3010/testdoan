from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    STATUS = (
        ('1', 'Mới'),
        ('2', 'Đã xem'),
    )
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    message = models.TextField(max_length=300)
    status = models.CharField(max_length=12,choices=STATUS, default=1)
    ip = models.CharField(blank=True, max_length=20)
    note = models.TextField(blank=True,max_length=300)
    create_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
class Subscribe(models.Model):
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.email