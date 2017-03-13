from django.db import models


class Organization(models.Model):
    organization_name = models.CharField(max_length=200)

    def __str__(self):
        return self.organization_name


class CourseSession(models.Model):
    session_name = models.CharField(max_length=200)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.session_name
