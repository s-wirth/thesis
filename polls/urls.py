from django.conf.urls import url

from polls.views import CreatePollView, IndexView, PollDetailView, ResultsView
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', PollDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^create_poll/$', CreatePollView.as_view(), name='create_poll'),
]