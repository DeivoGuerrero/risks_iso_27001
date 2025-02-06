from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def controls(request):
    return render(request, 'controls.html')

def categories(request):
    return render(request, 'categories.html')