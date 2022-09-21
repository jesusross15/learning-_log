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
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    # Page for adding a new Topic
    path('new_topic/', views.new_topic, name='new_topic'),
    
    # Page for adding a new Entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
]

