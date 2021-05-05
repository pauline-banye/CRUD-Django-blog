from django.urls import path
from .views import RegisterUser, EditUser, PasswordChange
from . import views


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('editprofile/', EditUser.as_view(), name='editprofile'),
    path('password/', PasswordChange.as_view(template_name='registration/reset_password.html')),
    path('password_success', views.password_success, name="password_success"),
    
]
