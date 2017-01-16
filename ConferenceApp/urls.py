from django.conf.urls import url
from . import views, auth


app_name = 'conference'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth.login, name='login'),
    url(r'^logout/$', auth.logout, name='logout'),
    url(r'^register/$', auth.register, name='register'),
    url(r'^sessions/new/$', views.SessionCreate.as_view(), name='session_create'),
    url(r'^sessions/$', views.SessionList.as_view(), name='sessions_list'),
    url(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionDetail.as_view(), name='session_detail'),
    url(r'^sessions/(?P<pk>[0-9]+)/change/$', views.SessionUpdate.as_view(), name='session_update'),
    url(r'^sessions/(?P<pk>[0-9]+)/delete/$', views.SessionDelete.as_view(), name='session_delete'),
]
