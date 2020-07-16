from django.conf.global_settings import EMAIL_HOST_USER
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ServerForm


# Create your views here.

def coming(request):
    # if request.method == 'POST' and email and name:
    #     send_mail(subject="Enquiries", content="Sign Ip", settings.EMAIL_HOST_USER, ['kike1996@hotmail.com'], fail_silently=False)
    if request.method == 'GET':
        form = ServerForm()
    else:
        form = ServerForm(request.POST)
        if form.is_valid():
            subject = 'Important'
            message = form.cleaned_data['email']
            try:
                send_mail(subject, message, EMAIL_HOST_USER, ['admin@learnhack.co.uk'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "index.html", {'form': form})
    return render(request, "index.html", {'form': form})

def index(request):
    return HttpResponse("<h1>MyClub Event Calendar</h1>")

def successView(request):
    return HttpResponse('Success! Thank you for your message.')