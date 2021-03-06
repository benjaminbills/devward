from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Project, Rating

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        field = '__all__'
        exclude = ['user']

class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class NewRatingForm(ModelForm):
    class Meta:
        model = Rating
        exclude = ['user','project']