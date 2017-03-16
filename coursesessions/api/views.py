from rest_framework.generics import ListAPIView, RetrieveAPIView

from coursesessions.models import CourseSession
from .serializers import SessionSerializer


class SessionListAPIView(ListAPIView):
    queryset = CourseSession.objects.all()
    serializer_class = SessionSerializer


class SessionDetailAPIView(RetrieveAPIView):
    queryset = CourseSession.objects.all()
    serializer_class = SessionSerializer