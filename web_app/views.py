from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def work_with_us(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        personalletter = request.POST.get('personalletter')
        subject = f'New Job Application from {firstname} {lastname}'
        body = f"""
        New job application received for ALFAHISS:

        Name: {firstname} {lastname}
        Email: {email}
        Phone: {phone}

        Personal Letter / Cover Letter:
        {personalletter}
        """
        
        email_message = EmailMessage(
            subject=subject,
            body=body,
            from_email=None,
            to=['enter your email'],
        )
        for field_name in ['cv', 'otherdocs']:
            files = request.FILES.getlist(field_name)
            for f in files:
                email_message.attach(f.name, f.read(), f.content_type)
        email_message.send()
        return redirect('home')
    return render(request, "work_with_us.html")

def contact_form(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        role = request.POST.get('role')
        company = request.POST.get('company')
        project = request.POST.get('project')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal-code')
        country = request.POST.get('country')
        
        subject = f'Customer contact form'
        body = f"""
        New customer contact form for ALFAHISS:
        
        Name: {firstname} {lastname}
        Email: {email}
        Phone: {phone}
        Role: {role}
        Company: {company}
        Project: {project}

        Building Address:
        {address}, {city}, {postal_code}
        Country: {country}
        """
        email_message = EmailMessage(
            subject=subject,
            body=body,
            from_email=None,
            to=['enter your email'], 
        )
        email_message.send()
        return redirect('home') # Ή σε μια σελίδα επιτυχίας (success)
    return render(request, "contact_form.html")
