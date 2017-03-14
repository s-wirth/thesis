from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView

from pollgroups.models import CourseSession


class IndexView(View):
    def get(self, request):
        sessions = CourseSession.objects.all()
        template = loader.get_template('pollgroups/index.html')
        context = {
            'sessions': sessions,
        }
        return HttpResponse(template.render(context, request))


class CreateSessionView(View):
    template = "pollgroups/create_session.html"

    @method_decorator(login_required)
    def post(self, request):
        pg_name = request.POST['session_name']
        new_session = CourseSession(pg_name=pg_name)
        new_session.save()
        init_admin = User.objects.get(pk=request.user.id)
        new_session.admins = [init_admin]
        assign_perm('make_poll', init_admin, new_session)
        new_session.save()

        return HttpResponseRedirect(reverse('pollgroups:detail', args=(new_session.id,)))

    def get(self, request):
        return render(request, self.template)


class CourseSessionDetailView(DetailView):
    template_name = "pollgroups/detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseSessionDetailView, self).get_context_data(**kwargs)
        session = CourseSession.objects.get(pk=self.kwargs['pk'])
        context['session'] = session
        context['questions'] = session.question_set.all()
        return context

    model = CourseSession


