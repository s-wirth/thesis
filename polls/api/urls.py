from django.conf.urls import url

from polls.api.views import PollListAPIView, PollDetailAPIView

urlpatterns = [
    url(r'^$', PollListAPIView.as_view(), name='poll-list'),
    url(r'^(?P<pk>[0-9]+)/$', PollDetailAPIView.as_view(), name='poll-detail'),
]