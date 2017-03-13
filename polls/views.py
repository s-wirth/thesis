from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from django.views import View
from django.views.generic import DetailView

from pollgroups.models import CourseSession
from polls.models import Question, Option


class IndexView(View):
    def get(self, request):
        template = loader.get_template('polls/index.html')
        questions = Question.objects.all()
        context = {
            'question_list': questions,
        }
        return HttpResponse(template.render(context, request))


class CreatePollView(View):
    template = "polls/create_poll.html"

    @method_decorator(login_required)
    def post(self, request):
        question_text = request.POST['question']
        session = CourseSession.objects.get(pk= request.POST['session'])
        new_question = Question(question_text=question_text, pub_date=now(), session=session)
        new_question.save()

        options_list = request.POST.getlist('options')
        for option in options_list:
            option_text = option
            new_option = Option(option_text=option_text, question=new_question)
            new_option.save()

        return HttpResponseRedirect(reverse('polls:detail', args=(new_question.id,)))

    def get(self, request):
        context = {'sessions': CourseSession.objects.all()}
        return render(request, self.template, context=context)


class PollDetailView(DetailView):
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        context = super(PollDetailView, self).get_context_data(**kwargs)
        question = Question.objects.get(pk=self.kwargs['pk'])
        context['options'] = question.option_set.all().order_by('pk')
        return context

    def post(self, request, *args, **kwargs):
        question = Question.objects.get(pk=self.kwargs['pk'])
        try:
            selected_choice = question.option_set.get(pk=request.POST['option'])
        except (KeyError, Option.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select an option.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    model = Question


class ResultsView(DetailView):
    template_name = "polls/results.html"
    model = Question
