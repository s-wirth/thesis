from rest_framework.generics import ListAPIView

from polls.models import Question
from .serializers import PollSerializer


class PollListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = PollSerializer
