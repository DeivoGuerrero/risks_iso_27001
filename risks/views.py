from django.shortcuts import render
from .models import control

# Create your views here.
def home(request):
    controls = control.objects.all()
    return render(request, 'home.html', {'controls': controls})

def controls(request):
    return render(request, 'controls.html')

def categories(request):
    return render(request, 'categories.html')

def sections(request):
    return render(request, 'sections.html')