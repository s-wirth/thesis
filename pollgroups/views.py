from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from pollgroups.models import CourseSession


def index(request):
    sessions = CourseSession.objects.all()
    template = loader.get_template('pollgroups/index.html')
    context = {
        'sessions': sessions,
    }
    return HttpResponse(template.render(context, request))



class CreatePollGroupView(View):
    template = "pollgroups/create_session.html"

    @method_decorator(login_required)
    def post(self, request):
        pg_name = request.POST['session_name']
        new_session = CourseSession(pg_name=pg_name)
        new_session.save()

        return HttpResponseRedirect(reverse('pollgroup:detail', args=(new_session.id,)))

    def get(self, request):
        return render(request, self.template)


class PollGroupDetailView(TemplateView):
    template = "pollgroups/create_session.html"

    def get_context_data(self, **kwargs):
        context = super(PollGroupDetailView, self).get_context_data(**kwargs)
        context['questions'] = self.session.question_set.all().order_by('pk')
        return context

    def get(self, request, *args, **kwargs):
        try:
            self.session = CourseSession.objects.get(pk=kwargs.get('pg_id'))
        except:
            raise Http404("Session does not exist")

        return render(request, self.template)


