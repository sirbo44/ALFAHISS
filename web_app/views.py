from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def work_with_us(request):
    return render(request, "work_with_us.html")

def contact_form(request):
    return render(request, "contact_form.html")
