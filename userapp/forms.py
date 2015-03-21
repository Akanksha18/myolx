from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from models import UserDetail, ItemDetail, ItemUpload

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',]

class ProfileImageForm(forms.Form):
    image = forms.FileField(label="Select an image to be uploaded")

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class UserDetailForm(ModelForm):
    class Meta:
        model = UserDetail
        fields=['first_name','last_name','phone_number','email_id']

class ItemDetailForm(ModelForm):
    class Meta:
        model = ItemDetail
        fields=['category','title','description','amount']

class ItemUploadForm(ModelForm):
    item_image = forms.FileField(label="Select an image to upload")
    
    class Meta:
        model = ItemDetail
        fields=['category','title','description','amount','item_image']
