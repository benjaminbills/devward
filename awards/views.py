from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.contrib import messages
from .forms import  CreateUserForm, ProfileForm, NewProjectForm, NewRatingForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Rating
from django.db.models import F


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
def getProjects(request):
    projects = Project.objects.all()
    
    # posts = profile.user.image_set.all()
    # total_post = posts.count()
    context = {'projects':projects }
    return render(request, 'project/projects.html', context)

@login_required(login_url='login')
def getProject(request, project_id):
    current_user = request.user
    project = Project.objects.get(pk=project_id)
    ratings = Rating.objects.filter(project__id__contains=project_id).annotate(avg_rating=(F('design')+ F('usability') +F('content'))/3).order_by('-avg_rating')
    logic = ratings.filter(user__username__icontains=current_user.username)
    content_list = []
    content_rating = 0
    design_list = []
    design_rating = 0
    usability_list = []
    usability_rating = 0
    for rating in ratings: 
        content_list.append(rating.content)
        content_rating = sum(content_list)/len(content_list)
        design_list.append(rating.design)
        design_rating = sum(design_list)/len(design_list)
        usability_list.append(rating.usability)
        usability_rating = sum(usability_list)/len(usability_list)
    
    if request.method == 'POST':
        form = NewRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = current_user
            rating.project = project
            rating.save()
        return redirect('get_project', project_id)

    else:
        form = NewRatingForm()
        context = {
            'project':project, 
            'form':form,
            'ratings':ratings, 
            'content_rating' : content_rating, 
            'design_rating' : design_rating, 
            'usability_rating' : usability_rating,
            'logic':logic

            }
        return render(request, 'project/project.html', context)