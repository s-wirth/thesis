from rest_framework.generics import ListAPIView

from polls.models import Question, Option
from .serializers import QuestionSerializer


class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer