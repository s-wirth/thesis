from rest_framework.generics import ListAPIView, RetrieveAPIView

from polls.models import Question
from .serializers import PollSerializer


class PollListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = PollSerializer


class PollDetailAPIView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = PollSerializer
