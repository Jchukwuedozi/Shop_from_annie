from django.db import models
from pathlib import Path
import uuid
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.#

def profile_pictures(instance, filename):
    file_path = Path(filename)
    filename,  ext = file_path.stem, file_path.suffix
    date = datetime.now()
    return f'profile_pictures/filename_{date}_{uuid.uuid4().hex}{ext}'

class GenderChoice(models.TextChoices):
    Male = 'M', 'Male'
    Female = 'F', 'Female'


class Profile(AbstractUser):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    gender = models.CharField(max_length=1, choices=GenderChoice)
    DOB = models.DateField()
    profile_picture = models.ImageField(upload_to=profile_pictures)
    date_joined = models.DateTimeField(auto_now=True)
    bio = models.TextField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','DOB',]

    def __str__(self):
        return self.username

