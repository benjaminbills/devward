from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Rating
# Create your tests here.
class ProfileTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Benjamin', email='ben@gmail.com', password='Bananna')
      self.user.save()
      self.profile = Profile(photo='http:cloudinary/devward/profile/ben.jpg', bio='I am amazing', user=self.user)
      
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.profile,Profile))  
  def test_save_method(self):
      self.profile.save_profile()     
      profile = Profile.objects.all()
      self.assertTrue(len(profile) > 0) 
  def tearDown(self):
      Profile.objects.all().delete()
  def delete_profile(self):
      self.profile.save_profile()
      profile=Profile.objects.all()
      self.assertEqual(len(profile), 1) 
      self.profile.delete_profile()
      del_profile=Profile.objects.all()
      self.assertEqual(len(del_profile),0)
  def test_update_profile(self):
      self.profile.save_profile()
      self.profile.update_profile(self.profile.id, bio='I am good', photo='http:image2')
      update_bio=Profile.objects.get(bio='I am good')
      update_profile_photo=Profile.objects.get(photo='http:image2')
      self.assertEqual(update_bio.bio,'I am good') 
      self.assertEqual(update_profile_photo.photo,'http:image2') 

class ProjectTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Benjamin', email='ben@gmail.com', password='Bananna')
      self.user.save()
      self.project = Project(image='http:cloudinary/PixelGram/profile/ben.jpg', title='peace', user=self.user, link='https://github.com/benjaminbills/devward', description='wake up')
      
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.project,Project))

  def test_save_method(self):
      self.project.save_project()     
      project = Project.objects.all()
      self.assertTrue(len(project) > 0) 
  def tearDown(self):
      Project.objects.all().delete()
  def delete_project(self):
      self.project.save_project()
      project=Project.objects.all()
      self.assertEqual(len(project), 1) 
      self.project.delete_project()
      del_project=project.objects.all()
      self.assertEqual(len(del_project),0)
  def test_update_project(self):
      self.project.save_project()
      self.project.update_project(self.project.id, title='good', image='http:image2', link='https://github.com/benjaminbills/devward', description='i am feeling good')
      update_title=Project.objects.get(title='good')
      update_image=Project.objects.get(image='http:image2')
      update_description=Project.objects.get(description='i am feeling good')
      self.assertEqual(update_title.title,'good') 
      self.assertEqual(update_image.image,'http:image2') 
      self.assertEqual(update_description.description,'i am feeling good') 


class RatingTestClass(TestCase):
  def setUp(self):
      self.user = User(username='Benjamin', email='ben@gmail.com', password='Bananna')
      self.user.save()
      self.project = Project(image='http:cloudinary/PixelGram/profile/ben.jpg', title='peace', user=self.user, link='https://github.com/benjaminbills/devward', description='wake up')
      self.project.save()
      self.rating = Rating(design = 6, content=7, usability=8, user = self.user, project = self.project)
      # Testing  instance
  def test_instance(self):
      self.assertTrue(isinstance(self.rating,Rating))

  def test_save_method(self):
      self.rating.save_rating()     
      rating = Rating.objects.all()
      self.assertTrue(len(rating) > 0) 

  def tearDown(self):
      Rating.objects.all().delete()
  def delete_rating(self):
      self.rating.save_rating()
      rating=Rating.objects.all()
      self.assertEqual(len(rating), 1) 
      self.rating.delete_rating()
      del_rating=Rating.objects.all()
      self.assertEqual(len(del_rating),0)
  
  def test_update_rating(self):
      self.rating.save_rating()
      self.rating.update_rating(self.rating.id, design=4, content=2, usability=9)
      update_design=Rating.objects.get(design=4)
      update_content=Rating.objects.get(content=2)
      update_usability=Rating.objects.get(usability=9)
      self.assertEqual(update_design.design,4)
      self.assertEqual(update_content.content,2) 
      self.assertEqual(update_usability.usability,9) 
