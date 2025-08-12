from django.db import models
from django.contrib.auth.models import User

class profilemodel(models.Model):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'

    user = models.OneToOneField(User , on_delete = models.CASCADE , verbose_name = 'کاربری' , related_name = 'profile')
    
    Gender_CHOICES = [
        ( 'Male', 'Male' ),
        ( 'Female' , 'Female' )
    ]
    Gender_status = models.CharField(max_length=6,choices = Gender_CHOICES , null = True , verbose_name = 'جنسیت کاربر' )
    ProfileImage = models.ImageField(upload_to='ProfileImage/' ,verbose_name = 'پروفایل' )
    
    Credit = models.IntegerField(verbose_name = 'اعتبار کاربر' , default = 0)
