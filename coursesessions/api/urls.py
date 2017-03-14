from django.conf.urls import url

from coursesessions.api.views import SessionListAPIView

urlpatterns = [
    url(r'^$', SessionListAPIView.as_view(), name='session-list'),
]