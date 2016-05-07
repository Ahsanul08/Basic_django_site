from django.conf.urls import url
from django.contrib import admin
from validation_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.show_signup_page, name="sign"),
    url(r'^log_in/$', views.show_login_page),
    url(r'^profile/$', views.do_signup, name="profile")
]
