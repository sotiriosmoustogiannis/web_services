from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import Shop


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


#Check thisyoutube video for uploading 2 or more files together
#Django Full Course - 11 - Upload file/multiple files, save file to the model
class UploadFileForm(forms.Form):
   file_before = forms.FileField()
   file_after = forms.FileField()

#file_before = efood from stand_alone
#file_after = nameefood from stand_alone

# class UploadFileForm(forms.ModelForm):
#     file = forms.FileField()

#     class Meta:
#         model = Shop    
#         fields = ['store_pickle']