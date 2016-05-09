from django.shortcuts import render
from django.http import HttpResponse
from validation_app.models import User
from django.db import IntegrityError
from validation_app.models import Acl
from subprocess import call

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
    request.META['USERNAME'] = user.user_name
    if user.password == request.POST.get('password'):
        if set_session(request, user.id):
            acl_access = Acl.objects.get(id = user.acl_id_id).category
            if acl_access == 'sticker_admin':
                return render(request, 'html/sticker_admin_profile.html')
            elif acl_access == 'web_admin':
                return render(request, 'html/web_admin_profile.html')
        else:
            return HttpResponse("Couldn't login for some unknown event")
    else:
        return HttpResponse("Your username and password didn't match.")


def make_ban_request(request):
    ban_seeked_content = request.POST.getlist('checks[]')
    print ban_seeked_content
    #u_id = User.objects.get(user_name=request.META.get('USERNAME')).id
    #if get_session(request,u_id):


    """
    host = ''

    if User.objects.get(user_name=username).acl_id == 'sticker_admin':
        host = 'http://ipvcloud.ringid.com'
    elif User.objects.get(user_name=username).acl_id == 'web_admin':
        host = 'http'
    """
    for individual_content in ban_seeked_content:
        call("curl -X BAN http://ipvcloud.ringid.com/{0}".format(individual_content),shell= True)
    return render(request,'html/form_output.html',{'ban_list': ban_seeked_content})

def show_login_page(request):
    return render(request, 'html/login_form.html')


def show_signup_page(request):
    return render(request, 'html/signup_form.html')


def logout(request):
    try:
        del request.session['SESSION_ID']
    except KeyError:
        pass
    return render(request, 'html/login_form.html')


def get_session(request,username):
    return request.session['SESSION_ID'] == User.objects.get(user_name = username).id

def set_session(request,u_id):
    try:
        request.session['SESSION_ID'] = u_id
    except:
        return False
    return True