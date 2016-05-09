from django.conf.urls import url
from django.contrib import admin
from validation_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.show_signup_page, name="sign_up"),
    url(r'^log_in/$', views.show_login_page, name="log_in"),
    url(r'^log_in/$', views.do_signup, name="sign_up_form"),
    url(r'^profile/$', views.show_profile, name="profile"),
    url(r'^ban_report/$',views.make_ban_request, name = "ban_url"),
    url(r'^log_in/$', views.logout, name= 'back_to_login')
]
