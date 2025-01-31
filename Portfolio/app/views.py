from django.shortcuts import render
from .models import Project, Documents

# Create your views here.

def home(request):
    projects = Project.objects.all()
    documents = Documents.objects.all()
    resume = "https://drive.google.com/file/d/1RBfFxlTMQfQ7dU3gTHxLSgi0qSgClXsM/view?usp=drive_link"
    return render(request, "home.html", {'projects':projects, 'documents':documents, 'resume':resume})