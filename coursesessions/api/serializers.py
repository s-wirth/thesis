from rest_framework.serializers import ModelSerializer

from coursesessions.models import CourseSession


class SessionSerializer(ModelSerializer):

    class Meta:
        model = CourseSession
        depth = 1
        fields = [
            'session_name',
            'admins',
            'question_set',
        ]