from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Profile(models.Model):
  photo=models.ImageField(upload_to='profile_photos/', default='profile_photos/default_rr8opn', blank=True)
  bio=models.TextField(max_length=1000, default='No Bio')
  user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)

class Project(models.Model):
  title=models.CharField(max_length=300)
  image=models.ImageField(upload_to='project_photos/', blank=True)
  link=models.URLField()
  description=models.TextField(max_length=1000)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  pub_date = models.DateTimeField(auto_now_add=True)

  @classmethod
  def posted_today(cls):
        today = dt.date.today()
        projects = cls.objects.filter(pub_date__date = today)
        return projects

class Rating(models.Model):
  design=models.FloatField(validators=[MaxValueValidator(10), MinValueValidator(1)])
  usability=models.FloatField(validators=[MaxValueValidator(10), MinValueValidator(1)])
  content=models.FloatField(validators=[MaxValueValidator(10), MinValueValidator(1)])
  project=models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
  user=models.ForeignKey(User, on_delete=models.CASCADE)
