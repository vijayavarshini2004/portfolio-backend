from rest_framework import viewsets
from .models import Profile, About, Skill, Project, HomePage, HomePageProject
from .serializers import ProfileSerializer, AboutSerializer, SkillSerializer, ProjectSerializer, HomePageSerializer, HomePageProjectSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

class HomePageProjectViewSet(viewsets.ModelViewSet):
    queryset = HomePageProject.objects.all()
    serializer_class = HomePageProjectSerializer
