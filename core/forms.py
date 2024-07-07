from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserSignUp(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, label='Full Name')
    admission_number = forms.CharField(max_length=20, required=True, label='Admission Number')
    course = forms.CharField(max_length=100, required=True, label='Course')
    year_of_studies = forms.IntegerField(required=True, label='Year of Studies')

    class Meta:
        model = User
        fields = ['username', 'full_name', 'admission_number', 'course', 'year_of_studies', 'email', 'password1', 'password2']
        labels = {
            'email': 'Email'
        }



# In forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileAdminForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)

    class Meta:
        model = Profile
        fields = '__all__'
