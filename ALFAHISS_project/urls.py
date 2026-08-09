from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from web_app import views # Import τα views απευθείας από εδώ

urlpatterns = [
    path('i18n/', set_language, name='set_language'),
    path('admin/', admin.site.urls),
]

# Εδώ μπαίνουν όλα τα URL της εφαρμογής σου
urlpatterns += i18n_patterns(
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('work-with-us/', views.work_with_us, name='work-with-us'),
    path('contact-form/', views.contact_form, name='contact-form'),
    prefix_default_language=False,
)