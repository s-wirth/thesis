from django.conf.urls import url

from polls.api.views import QuestionListAPIView
from polls.views import CreatePollView, IndexView, PollDetailView, ResultsView
from . import views

urlpatterns = [
    url(r'^$', QuestionListAPIView.as_view(), name='question-list'),
]