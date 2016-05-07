from django.shortcuts import render
from django.http import HttpResponse
from validation_app.models import User

# Create your views here.

def show_signup_page(request):
    render(request,'validation_templates/signup_form.html')

def view_profile(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        

    else:
        return HttpResponse("Please reuest with proper username and password.")
    render(request,'validation_templates/profile.html',{'username' : username})