from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {"page": "home"}
    return render(request, "home.html", context)
def services(request):
    context = {"page": "services"}
    return render(request, "services.html", context)
def about(request):
    context = {"page": "about"}
    return render(request, "about.html", context)
def contact(request):
    context = {"page": "contact"}
    return render(request, "contact.html", context)
def quote(request):
    context = {"page": "quote"}
    return render(request, "quote.html", context)
