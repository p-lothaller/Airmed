from django.contrib import admin
from .models import Profile, calorie_counter, weight_counter, exercise

# Register your models here.
admin.site.register(Profile)
admin.site.register(calorie_counter)
admin.site.register(weight_counter)
admin.site.register(exercise)
