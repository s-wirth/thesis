from django.conf.urls import url

from pollgroups.views import PollGroupDetailView, CreatePollGroupView
from polls.views import CreatePollView
from . import views

app_name = 'pollgroups'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pollgroup_id>[0-9]+)/$', PollGroupDetailView.as_view(), name='detail'),
    url(r'^create_poll/$', CreatePollGroupView.as_view(), name='create_poll'),
]