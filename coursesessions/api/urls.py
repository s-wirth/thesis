from django.conf.urls import url

from coursesessions.api.views import SessionListAPIView, SessionDetailAPIView

urlpatterns = [
    url(r'^$', SessionListAPIView.as_view(), name='session-list'),
    url(r'^(?P<pk>[0-9]+)/$', SessionDetailAPIView.as_view(), name='session-detail'),
]
