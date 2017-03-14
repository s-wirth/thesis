from django.conf.urls import url

from polls.api.views import PollListAPIView

urlpatterns = [
    url(r'^$', PollListAPIView.as_view(), name='poll-list'),
]