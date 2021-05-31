from rest_framework import serializers
from awards.models import Profile, Project

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields ='__all__'

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields ='__all__'