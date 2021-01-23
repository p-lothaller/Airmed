from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, calorie_counter, weight_counter, exercise

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

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Gender', 'weight', 'height', 'birth_date', 'location', 'image']

class CalorieForm(forms.ModelForm):
    class Meta:
        model = calorie_counter
        fields = ['cal_amount']

class WeightForm(forms.ModelForm):
    class Meta:
        model = weight_counter
        fields = ['weight_amount']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = exercise
        fields = ['reps', 'sets', 'one_rep_max']
