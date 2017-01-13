from django.conf.urls import url
from . import views, auth


app_name = 'conference'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth.login, name='login'),
    url(r'^logout/$', auth.logout, name='logout'),
    url(r'^register/$', auth.register, name='register'),

]
