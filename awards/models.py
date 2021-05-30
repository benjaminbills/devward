from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  photo=models.ImageField(upload_to='profile_photos/', default='profile_photos/default_nlfwhd', blank=True)
  bio=models.TextField(max_length=1000, default='No Bio')
  user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
