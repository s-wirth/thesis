from django.contrib.auth.models import User
from django.db import models


class CourseSession(models.Model):
    session_name = models.CharField(max_length=200)
    admins = models.ManyToManyField(User, related_name='admins')
    participants = models.ManyToManyField(User, related_name='participants')

    def __str__(self):
        return self.session_name

    class Meta:
        permissions = (
            ('make_poll', 'Make Poll'),
        )
