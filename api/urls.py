from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
  path('project-list', views.projectList, name='project-list'),
  path('profile-list', views.profileList, name='profile-list')
]
