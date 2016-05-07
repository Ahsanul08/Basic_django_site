from django.conf.urls import url
from django.contrib import admin
from validation_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sign_up/$', views.show_signup_page),
    url(r'^profile/$', views.)
]
