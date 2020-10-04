from django.urls import path

from user_profiles import views

urlpatterns = [
    path('api/profile', views.UserProfile.as_view()),
]
