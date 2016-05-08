from django.shortcuts import render
from django.http import HttpResponse
from validation_app.models import User
from django.db import IntegrityError
from validation_app.models import Acl

# Create your views here.

def show_signup_page(request):
    return render(request, 'html/signup_form.html')


def do_signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        acl_instance = Acl.objects.get(id=1)
        row = User(user_name=username, password = password, acl_id = acl_instance)
        try:
            row.save()
        except IntegrityError:
            return HttpResponse("Sorry! Username already exist!! Try a diffrent Username!!!")
        except:
            return HttpResponse("Sorry! User couldn't be created!!")
    else:
        return HttpResponse("Please request with proper username and password.")
    return render(request, 'html/login_form.html')


def show_profile(request):
    user = User.objects.get(user_name=request.POST.get('username'))
    if user.password == request.POST.get('password'):
        if set_session(request, user.id):
            return render(request, 'html/profile.html',{'user_name' : user.user_name})
        else:
            return HttpResponse("Couldn't login for some unknown event")
    else:
        return HttpResponse("Your username and password didn't match.")


def show_login_page(request):
    return render(request, 'html/login_form.html')


def show_signup_page(request):
    return render(request, 'html/signup_form.html')


def logout(request):
    try:
        del request.session['session_id']
    except KeyError:
        pass
    return render(request, 'html/login_form.html')


def get_session(request,username):
    return request.session['session_id'] == User.objects.get(user_name = username).id

def set_session(request,u_id):
    try:
        request.session['session_id'] = u_id
    except:
        return False
    return True