from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200)

    def __string__(self):
        return "lol"
