from django.conf.urls import url

from coursesessions.views import CourseSessionDetailView, CreateSessionView, IndexView

app_name = 'coursesessions'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', CourseSessionDetailView.as_view(), name='detail'),
    url(r'^create_session/$', CreateSessionView.as_view(), name='create_session'),
]