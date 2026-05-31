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
    if request.method == "POST":
        customer_name = request.POST.get('full-name')
        customer_email = request.POST.get('email')
        customer_phone = request.POST.get('phone')
        customer_company = request.POST.get('company')
        customer_service = request.POST.get('service')
        customer_message = request.POST.get('message')
        print(customer_name, customer_email, customer_phone, customer_company, customer_service, customer_message)
        context = {"page": "quote"}
        return render(request, "quote.html", context)
    context = {"page": "quote"}
    return render(request, "quote.html", context)
