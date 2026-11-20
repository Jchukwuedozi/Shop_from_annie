from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'first_name', 'last_name', 
              'gender', 'DOB', 'profile_picture',
              'bio']
    list_display = ['username', 'email', 'first_name', 'last_name', 
              'gender', 'DOB', 'profile_picture',
              'bio', 'date_joined']
    search_fields = ['username', 'email']


