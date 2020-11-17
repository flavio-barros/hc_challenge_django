from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'reports', views.ReportViewSet, basename='Report')
router.register(r'users', views.UserViewSet, basename='User')

urlpatterns = [
    path('', include(router.urls)),
]