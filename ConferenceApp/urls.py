from django.conf.urls import url
from . import views, auth


app_name = 'conference'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth.login, name='login'),
    url(r'^logout/$', auth.logout, name='logout'),
    url(r'^register/$', auth.register, name='register'),
    url(r'^submit/$', views.submit_session, name='submit_session'),
    url(r'^sessions/$', views.SessionList.as_view(), name='sessions_list'),
    url(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionDetail.as_view(), name='session_detail'),
]
