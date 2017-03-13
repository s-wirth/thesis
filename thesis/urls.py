from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('homepage.urls')),
    url(r'^polls/', include('polls.urls')),
]

urlpatterns += staticfiles_urlpatterns()
