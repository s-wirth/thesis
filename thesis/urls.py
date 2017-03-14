from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('homepage.urls')),
    url(r'^pollgroups/', include('pollgroups.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^api/polls/', include('polls.api.urls')),
]

urlpatterns += staticfiles_urlpatterns()
