"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# These 2 lines import a module and a function to manage URLS for the admin site
from django.contrib import admin
from django.urls import path, include

# The body of the files defines the urlpatterns variable
# which includes sets of URLS from the apps in the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls'))
    path('', include('learning_logs.urls')),
]
# The code above includes the module admin.site.urls that defines all the URLS that can be
# requested from the admin site

