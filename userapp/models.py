from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import ModelForm

class ProfileImage(models.Model):
    image = models.FileField(upload_to='profile/%Y/%m/%d')

class Photo(models.Model):
   photo = models.ImageField(upload_to="photos")
