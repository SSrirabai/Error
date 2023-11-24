# BlogNVlog/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from blog.views import post_list, RegisterView  # Import your RegisterView here
from django.contrib.auth.views import LoginView, LogoutView  # Import authentication views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', post_list, name='post_list'),
    
    # Authentication views
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='blog/register.html'), name='register'),
    
    # Add other paths as needed
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
