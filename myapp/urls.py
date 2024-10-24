from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, AboutViewSet, SkillViewSet, ProjectViewSet, HomePageViewSet, HomePageProjectViewSet

# Define the router and register the viewsets
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'about', AboutViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)  # Project routes will be created automatically
router.register(r'homepages', HomePageViewSet)
router.register(r'homepage-projects', HomePageProjectViewSet)

# Include the router.urls in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
