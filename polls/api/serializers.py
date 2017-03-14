from rest_framework.serializers import ModelSerializer

from polls.models import Question


class PollSerializer(ModelSerializer):

    class Meta:
        model = Question
        depth = 1
        fields = [
            'question_text',
            'session',
            'pub_date',
            'option_set',
        ]