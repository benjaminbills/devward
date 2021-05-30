from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.contrib import messages
from .forms import  CreateUserForm, ProfileForm, NewProjectForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Project


# Create your views here.
def home(request):
  return render(request, 'home.html')

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'registration/login.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Profile.objects.create(
                user=user,
            )
            # send_welcome_email(user.username,user.email)
            messages.success(request, 'Account was creates for ' + username )
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def accountSettings(request):
	profile = request.user.profile
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES,instance=profile)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'profile/profile_edit.html', context)

@login_required(login_url='login')
def userPage(request, user_id):
    profile = Profile.objects.get(user=user_id)
    
    # posts = profile.user.image_set.all()
    # total_post = posts.count()
    context = {'profile':profile }
    return render(request, 'profile/profile.html', context)

@login_required(login_url='login')
def addProject(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    context = {'form':form}
    return render(request, 'project/add_project.html', context)

@login_required(login_url='login')
def viewProjects(request):
    projects = Project.objects.all()
    
    # posts = profile.user.image_set.all()
    # total_post = posts.count()
    context = {'projects':projects }
    return render(request, 'project/projects.html', context)