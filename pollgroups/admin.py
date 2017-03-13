from django.contrib import admin

from .models import Organization, CourseSession

admin.site.register(Organization)
admin.site.register(CourseSession)