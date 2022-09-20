# Defines URL patterns for learning_logs

# importing the path function that is needed when mapping URLS to views
from django.urls import path
# importing the views module (the dot make it so Python imports the views.py module from the same
# directory as the current urls.py module)
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),
    
]

