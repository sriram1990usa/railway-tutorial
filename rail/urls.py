"""rail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path,include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns =[
    url(r'^admin/', admin.site.urls),
    url(r'^login',user_views.login_request, name = 'login'),
    url(r'^register/', user_views.register, name="register"),
    url(r'^logout', user_views.logout_request, name="logout"),
    path('', include('home.urls')), 
]
'''
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('login', user_views.login_request, name='login'),
    path('register', user_views.register, name="register"),
    path('logout', user_views.logout_request, name="logout"),
    path('home/logout', user_views.logout_request, name="logout"),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('home.urls')),   
] 
'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
