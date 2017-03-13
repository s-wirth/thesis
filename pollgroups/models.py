from django.db import models


class PollGroup(models.Model):
    pg_name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Organization(PollGroup):

    def __str__(self):
        return self.pg_name


class CourseSession(PollGroup):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pg_name
