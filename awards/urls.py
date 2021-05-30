from django.urls import path
from . import views


urlpatterns = [
  path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
  path('logout/', views.logoutUser, name="logout"),
  path('', views.home, name='home' ),
  path('account/', views.accountSettings, name='account'),
  path('user/<int:user_id>', views.userPage, name='user_page'),

]
