from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'first_name', 'last_name', 
              'gender', 'DOB', 'profile_picture',
              'bio']