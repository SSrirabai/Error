# blog/urls.py
from django.urls import path
from .views import post_list, RegisterView, LoginView, LogoutView  # Import LoginView and LogoutView

urlpatterns = [
    path('', post_list, name='post_list'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='blog/register.html'), name='register'),
    # Add other paths as needed
]
