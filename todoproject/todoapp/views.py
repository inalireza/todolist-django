from django.shortcuts import render

# Create your views here.
from .models import TodoItem

def HomeView(request):
    return render(request, 'todoapp/home.html')