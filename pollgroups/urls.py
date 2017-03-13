from django.conf.urls import url

from pollgroups.views import CourseSessionDetailView, CreateSessionView
from . import views

app_name = 'pollgroups'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', CourseSessionDetailView.as_view(), name='detail'),
    url(r'^create_session/$', CreateSessionView.as_view(), name='create_session'),
]