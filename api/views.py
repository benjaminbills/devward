from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from awards.models import Profile, Project
from .serializers import ProjectSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Profiles':'/profile-list/',
		'Projects':'/project-list/',
		}

	return Response(api_urls)

@api_view(['GET'])
def projectList(request):
  projects = Project.objects.all().order_by('-id')
  serializer = ProjectSerializer(projects, many=True)
  return Response(serializer.data)
