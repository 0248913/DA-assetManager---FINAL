"""
assetManager02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from AssetManagerApp import views

urlpatterns = [

    path('deleteSpace/<int:space_id>/', views.deleteSpace, name="deleteSpace"),
    
    path('admin/', admin.site.urls),
    
    path('', views.sitehome, name=""),

    path('calendar', views.calendar, name="calendar"),
    
    path('register', views.register, name="register"),

    path('login', views.login, name="login"),
    
    path('dashboard', views.dashboard, name="dashboard"),

    path('logout', views.logout, name="logout"),
    
    path('newLog/<int:space_id>/', views.newLog, name="newLog"),
    
    path('editLog/<int:log_id>/<int:space_id>/', views.editLog, name="editLog"),
     
    path('deleteLog/<int:log_id>//<int:space_id>/', views.deleteLog, name="deleteLog"),
  
    path('homepage', views.homepage, name='homepage'),
    
    path('spaceCreate', views.spaceCreate, name='spaceCreate'),
    
    path('dashboard/<int:space_id>/', views.dashboard, name= 'dashboard'),
    
    path('spaceManage/<int:space_id>/members/', views.spaceManage, name='spaceManage'),
    
    path('settings', views.settings, name='settings'),
    
   path('pinSpace/<int:space_id>/', views.pinSpace, name='pinSpace'),
    
   path('unpinSpace/<int:space_id>/', views.unpinSpace, name='unpinSpace'),
    
    path('Profile', views.Profile, name='Profile'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

