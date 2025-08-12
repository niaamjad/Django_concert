from django.db import models
from account.models import profilemodel

class concertmodel(models.Model):
    class Meta:
        verbose_name = 'کنسرت'
        verbose_name_plural = 'کنسرت'
    Name = models.CharField(max_length=100 , verbose_name = 'نام کنسرت')
    SingerName = models.CharField(max_length=100 , verbose_name = 'نام خواننده')
    Lenght = models.IntegerField(verbose_name = 'طول زمان برگزاری کنسرت')  
    Poster = models.ImageField(upload_to='PosterImage/' , null=True , verbose_name = 'پوستر')
    


    def __str__(self):
        return self.Name + " - " + self.SingerName + " (" + str(self.Lenght) + " mins)"
    

class locationmodel(models.Model):
    class Meta:
        verbose_name = 'مکان برگزای کنسرت'
        verbose_name_plural ='مکان برگزای کنسرت'
    Name = models.CharField(max_length=100 , verbose_name = 'نام محل برگزاری کنسرت')
    Address = models.CharField(max_length=200 , verbose_name = 'آدرس محل برگزاری کنسرت')
    Phone = models.CharField(max_length=15,null=True , verbose_name = 'شماره تماس')
    Capacity = models.IntegerField(verbose_name = 'ظرفیت سالن')

    def __str__(self):
        return self.Name + " - " + self.Address + " (Capacity: " + str(self.Capacity) + ")"
    
class timemodel(models.Model):
    class Meta:
        verbose_name = 'زمان فروش بلیت کنسرت'
        verbose_name_plural = 'زمان فروش بلیت کنسرت'
    Concert = models.ForeignKey(concertmodel, on_delete=models.PROTECT , verbose_name = 'کنسرت' )
    Location = models.ForeignKey(locationmodel, on_delete=models.PROTECT , verbose_name = 'مکان برگزاری کنسرت')
    StartDateTime = models.DateTimeField(verbose_name = 'زمان شروع فروش بلیت')
    Seats = models.IntegerField(verbose_name = 'ظرفیت صندلی ها' )

    status_choices = [
        ('Start',  'زمان فروش بلیت آغاز شده است'),
        ('End', 'زمان فروش بلیت تمام شده است'),
        ('Cancel', 'کنسرت کنسل شده است'),
        ('Sale', 'درحال فروش بلیت')
    ]
    Status = models.CharField(choices = status_choices , null = True , verbose_name = 'وضعیت فروش بلیت' )


    def __str__(self):
        return f"{self.Concert.Name} at {self.Location.Name} on {self.StartDateTime.strftime('%Y-%m-%d %H:%M')}"
    
    

class Ticketmodel(models.Model):
    class Meta:
        verbose_name = 'بلیط کنسرت'
        verbose_name_plural = 'بلیط کنسرت'
    Profile = models.ForeignKey(profilemodel, on_delete=models.PROTECT , verbose_name = 'پروفایل' )
    Time = models.ForeignKey(timemodel, on_delete=models.PROTECT , verbose_name = 'زمان بلیت')
    Name = models.CharField(max_length=100 , verbose_name = 'نام بلیت' )
    Price = models.IntegerField(verbose_name = 'قیمت بلیت')
    TicketImage = models.ImageField(upload_to='TicketImage/' , verbose_name = 'بلیت' )

    def __str__(self):
        return f"Ticket for {self.Name} - {self.Profile.Name} {self.Profile.FamilyName} at {self.Time.StartDateTime.strftime('%Y-%m-%d %H:%M')}"