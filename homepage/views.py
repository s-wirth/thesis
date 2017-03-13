from django.http import HttpResponse
from django.template import loader


def homepage(request):
    template = loader.get_template('homepage/homepage.html')
    return HttpResponse(template.render({}, request))
