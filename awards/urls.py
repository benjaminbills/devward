from django.urls import path
from . import views


urlpatterns = [
  path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
  path('logout/', views.logoutUser, name="logout"),
  path('', views.home, name='home' ),
  path('account/', views.accountSettings, name='account'),
  path('user/<int:user_id>', views.userPage, name='user_page'),
  path('add_project/', views.addProject, name='add_project'),
  path('get_projects/', views.getProjects, name='get_projects'),
  path('get_project/<str:project_id>', views.getProject, name='get_project'),
  path('search/', views.search, name='search'),
]
