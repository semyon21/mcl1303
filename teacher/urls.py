from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns =[
    url(r'^login/$', login, {'template_name': 'teacher/login.html'}, name = 'login'),
    url(r'^logout/$', views.logout_view, name = 'logout'), 
    url(r'^register/$', views.register, name = 'register'),
    url(r'^send_message/$', views.send_message, name = 'send_message'),
]
