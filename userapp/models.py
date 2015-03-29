from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import ModelForm

class ProfileImage(models.Model):
    image = models.FileField(upload_to='profile/%Y/%m/%d')

# class Photo(models.Model):
#    photo = models.ImageField(upload_to="photos")

class UserDetail(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=10,unique=True)
    email_id = models.EmailField(max_length=50,unique=True)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class ItemDetail(models.Model):
    user = models.ForeignKey(User)
    GADGET = 'GDT'
    BOOK = 'BOK'
    ELECTRONICS = 'ELC'
    OTHER = 'OTH'
    CATEGORY_CHOICES = (
        (GADGET, 'Gadget'),
        (BOOK, 'Book'),
        (ELECTRONICS, 'Electronics'),
        (OTHER, 'Other'),
    )
    category = models.CharField(max_length=3,
                                      choices=CATEGORY_CHOICES,
                                      default=OTHER)

    title = models.CharField(max_length=50) 
    description = models.TextField(max_length=50)
    amount = models.IntegerField(max_length=10,unique=True)
    
    def __unicode__(self):
        return u"%s %s" % (self.title, self.category)


class ItemUpload(models.Model):
    user = models.ForeignKey(User)
    GADGET = 'GDT'
    BOOK = 'BOK'
    ELECTRONICS = 'ELC'
    OTHER = 'OTH'
    CATEGORY_CHOICES = (
        (GADGET, 'Gadget'),
        (BOOK, 'Book'),
        (ELECTRONICS, 'Electronics'),
        (OTHER, 'Other'),
    )
    category = models.CharField(max_length=3,
                                      choices=CATEGORY_CHOICES,
                                      default=OTHER)

    title = models.CharField(max_length=50) 
    description = models.TextField(max_length=50)
    amount = models.IntegerField(max_length=10,unique=True)
    item_image = models.FileField(upload_to='static/userimg')
    
    def __unicode__(self):
        return u"%s %s" % (self.title, self.category)
# query = Members.objects.all().query
# query.group_by = ['category']
# results = QuerySet(query=query, model=User)

# from django.db.models import Count
# Members.objects.values('designation').annotate(dcount=Count('designation'))