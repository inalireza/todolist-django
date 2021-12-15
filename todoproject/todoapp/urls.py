from django.urls import path
from .views import HomeView
app_name = 'todoapp'

urlpatterns = [
    path('',HomeView, name="home_url"),
    
]

