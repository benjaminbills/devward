from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Profile(models.Model):
  photo=models.ImageField(upload_to='profile_photos/', default='profile_photos/default_rr8opn', blank=True)
  bio=models.TextField(max_length=1000, default='No Bio')
  user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  def save_profile(self):
        self.save()
  def delete_profile(self):
        self.delete()
  @classmethod
  def update_profile(cls, profile_id, bio, photo):
        profile = cls.objects.filter(pk=profile_id).update(bio=bio,photo=photo)
        return profile
  @classmethod
  def get_profile(cls,username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile
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
  
  def save_project(self):
    self.save()
  
  def delete_project(self):
        self.delete()

  @classmethod
  def update_project(cls, id, title, image, link, description):
        project = cls.objects.filter(pk=id).update(title=title,image=image, link=link, description=description)
        return project

class Rating(models.Model):
  design=models.FloatField(validators=[MaxValueValidator(10), MinValueValidator(1)])
  usability=models.FloatField(validators=[MaxValueValidator(10), MinValueValidator(1)])
  content=models.FloatField(validators=[MaxValueValidator(10), MinValueValidator(1)])
  project=models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  def save_rating(self):
          self.save()

  def delete_rating(self):
          self.delete()

  @classmethod
  def update_rating(cls, id, design, usability, content):
          rating = cls.objects.filter(pk=id).update(design=design, usability=usability, content=content)
          return rating